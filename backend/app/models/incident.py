from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.db.database import Base


class Incident(Base):
    """
    Stores industrial incidents detected by AI.
    """

    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String)

    zone = Column(String)

    severity = Column(String)

    status = Column(String, default="Open")

    created_at = Column(DateTime, default=datetime.utcnow)