from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.db.database import Base


class Permit(Base):
    __tablename__ = "permits"

    id = Column(Integer, primary_key=True, index=True)

    permit_number = Column(String, unique=True, nullable=False)

    permit_type = Column(String, nullable=False)

    work_location = Column(String, nullable=False)

    issued_to = Column(String, nullable=False)

    approved_by = Column(String, nullable=False)

    status = Column(String, default="Pending")

    created_at = Column(DateTime, default=datetime.utcnow)

    expires_at = Column(DateTime)