from fastapi import APIRouter

from app.services.database_service import DatabaseService

router = APIRouter(
    prefix="/api/alerts",
    tags=["Alerts"]
)


@router.get("/")
def get_alerts():

    return {
        "success": True,
        "count": len(DatabaseService.get_alerts()),
        "alerts": DatabaseService.get_alerts()
    }