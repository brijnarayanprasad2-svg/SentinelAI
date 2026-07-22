from fastapi import APIRouter

from app.services.database_service import DatabaseService

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"],
)


@router.get("/")
def dashboard():

    return {
        "success": True,
        "data": DatabaseService.dashboard_summary()
    }


@router.get("/database")
def database_info():

    return {
        "success": True,
        "data": DatabaseService.database_info()
    }


@router.get("/health")
def database_health():

    return {
        "success": DatabaseService.check_connection(),
        "database": "SQLite"
    }