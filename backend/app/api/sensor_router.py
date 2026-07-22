from fastapi import APIRouter

from app.ai.decision_engine import DecisionEngine
from app.services.database_service import DatabaseService

router = APIRouter(
    prefix="/api/sensors",
    tags=["Sensors"],
)


@router.get("/latest")
def latest():

    try:

        sensors = DatabaseService.get_latest()

        # AI Decision from latest sensors
        decision = None

        if sensors:
            decision = DecisionEngine.analyze(sensors)

        # -----------------------------
        # Sensors
        # -----------------------------

        sensor_data = []

        for sensor in sensors:

            sensor_data.append({

                "id": sensor.id,

                "sensor_name": sensor.sensor_name,

                "sensor_type": sensor.sensor_type,

                "zone": sensor.zone,

                "value": sensor.value,

                "unit": sensor.unit,

                "status": sensor.status,

                "timestamp": (
                    sensor.timestamp.isoformat()
                    if sensor.timestamp
                    else None
                ),

            })

        # -----------------------------
        # Alerts
        # -----------------------------

        alerts = DatabaseService.get_alerts()

        alert_data = []

        for alert in alerts:

            alert_data.append({

                "id": alert.id,

                "title": alert.title,

                "zone": alert.zone,

                "severity": alert.severity,

                "status": alert.status,

                "recommendation": alert.recommendation,

            })

        # -----------------------------
        # Incident
        # -----------------------------

        incident = DatabaseService.get_latest_incident()

        incident_data = None

        if incident:

            incident_data = {

                "id": incident.id,

                "title": incident.title,

                "description": incident.description,

                "zone": incident.zone,

                "severity": incident.severity,

                "status": incident.status,

            }

        # -----------------------------
        # Final Response
        # -----------------------------

        return {

            "success": True,

            "count": len(sensor_data),

            "sensors": sensor_data,

            "decision": decision,

            "alerts": alert_data,

            "incident": incident_data,

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e),

        }