from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.db.database import Base


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)

    sensor_name = Column(String, nullable=False)

    sensor_type = Column(String, nullable=False)

    zone = Column(String, nullable=False)

    value = Column(Float, nullable=False)

    unit = Column(String, nullable=False)

    status = Column(String, nullable=False)

    timestamp = Column(DateTime, default=datetime.utcnow)