from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.services.sensor_service import generate_sensor_data

router = APIRouter(
    tags=["Live Monitoring"]
)


class ConnectionManager:

    def __init__(self):
        self.connections = []

    async def connect(self, websocket: WebSocket):

        await websocket.accept()

        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):

        if websocket in self.connections:
            self.connections.remove(websocket)

    async def broadcast(self, data):

        disconnected = []

        for connection in self.connections:

            try:

                await connection.send_json(data)

            except Exception:

                disconnected.append(connection)

        for connection in disconnected:

            self.disconnect(connection)


manager = ConnectionManager()


@router.websocket("/ws/sensors")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:

        while True:

            data = generate_sensor_data()

            await manager.broadcast(data)

    except WebSocketDisconnect:

        manager.disconnect(websocket)