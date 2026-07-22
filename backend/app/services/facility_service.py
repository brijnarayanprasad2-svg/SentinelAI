from app.models.facility import Facility
from app.services.database_service import DatabaseService


class FacilityService:

    @staticmethod
    def get_all():

        return DatabaseService.get_facilities()

    @staticmethod
    def create(name, location, manager):

        facility = Facility(
            name=name,
            location=location,
            manager=manager,
            status="Active",
        )

        DatabaseService.save_facility(facility)

        return facility