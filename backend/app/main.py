import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.db.database import create_tables

from app.api import sensor_router
from app.api.alert_router import router as alert_router
from app.api.incident_router import router as incident_router
from app.api.dashboard import router as dashboard_router
from app.api.facility_router import router as facility_router
from app.api.permit_router import router as permit_router
from app.api.auth import router as auth_router
from app.api.user import router as user_router
from app.api.websocket import router as websocket_router

from app.simulator.sensor_simulator import sensor_simulator


# ==========================================================
# FastAPI Application
# ==========================================================

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
)


# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# Register Routers
# ==========================================================

app.include_router(sensor_router)
app.include_router(alert_router)
app.include_router(incident_router)
app.include_router(dashboard_router)
app.include_router(facility_router)
app.include_router(permit_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(websocket_router)


# ==========================================================
# Home API
# ==========================================================

@app.get("/", tags=["Home"])
async def home():
    return {
        "success": True,
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running Successfully 🚀",
        "message": "Welcome to SentinelAI",
    }


# ==========================================================
# Health API
# ==========================================================

@app.get("/health", tags=["Health"])
async def health():
    return {
        "success": True,
        "application": settings.APP_NAME,
        "database": "SQLite Connected",
        "status": "Healthy",
    }


# ==========================================================
# Startup Event
# ==========================================================

@app.on_event("startup")
async def startup_event():

    create_tables()

    print("\n" + "=" * 60)
    print("🚀 SentinelAI Backend Started Successfully")
    print("✅ SQLite Database Ready")
    print("📡 Sensor Simulator Running")
    print("=" * 60 + "\n")

    asyncio.create_task(sensor_simulator())