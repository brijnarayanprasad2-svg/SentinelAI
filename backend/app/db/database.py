from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# ======================================================
# Database Configuration
# ======================================================

DATABASE_URL = "sqlite:///./sentinelai.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


# ======================================================
# Database Session Dependency
# ======================================================

def get_db():
    """
    Creates a new database session.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ======================================================
# Create Database Tables
# ======================================================

def create_tables():
    """
    Import only implemented models.
    Add new models here after creating them.
    """

    from app.models.sensor import Sensor
    from app.models.alert import Alert
    from app.models.incident import Incident
    from app.models.user import User
    
    Base.metadata.create_all(bind=engine)

    print("✅ SQLite Database Ready")