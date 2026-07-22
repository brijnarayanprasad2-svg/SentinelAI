from fastapi import APIRouter

from app.services.database_service import DatabaseService

router = APIRouter(
    prefix="/api/incidents",
    tags=["Incidents"]
)


@router.get("/")
def get_incidents():

    return {
        "success": True,
        "count": len(DatabaseService.get_incidents()),
        "incidents": DatabaseService.get_incidents()
    }