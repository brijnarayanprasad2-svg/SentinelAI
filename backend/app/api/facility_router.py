from fastapi import APIRouter

from app.services.facility_service import FacilityService

router = APIRouter(
    prefix="/api/facilities",
    tags=["Facilities"],
)


@router.get("/")
def all_facilities():

    return FacilityService.get_all()


@router.post("/")
def create_facility():

    return FacilityService.create(
        "Plant A",
        "Delhi",
        "Admin",
    )
