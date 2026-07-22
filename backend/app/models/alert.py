from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    zone = Column(String, nullable=False)

    severity = Column(String, nullable=False)

    status = Column(String, default="Open")

    recommendation = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)