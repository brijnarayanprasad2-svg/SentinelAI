from pydantic import BaseModel


class SensorResponse(BaseModel):

    sensor_name: str

    sensor_type: str

    zone: str

    value: float

    unit: str

    status: str