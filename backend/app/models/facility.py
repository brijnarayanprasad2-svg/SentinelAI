from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Facility(Base):
    __tablename__ = "facilities"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    location = Column(String, nullable=False)

    manager = Column(String, nullable=False)

    status = Column(String, default="Active")