from fastapi import APIRouter

from app.services.permit_service import PermitService

router = APIRouter(
    prefix="/api/permits",
    tags=["Permits"],
)


@router.post("/")
def create():

    return PermitService.create_permit()


@router.get("/")
def all_permits():

    return PermitService.get_all()