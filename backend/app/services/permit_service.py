from datetime import datetime, timedelta
import uuid

from app.models.permit import Permit
from app.services.database_service import DatabaseService


class PermitService:

    @staticmethod
    def create_permit():

        permit = Permit(

            permit_number=f"PTW-{uuid.uuid4().hex[:6].upper()}",

            permit_type="Hot Work",

            work_location="Boiler",

            issued_to="Operator",

            approved_by="Safety Manager",

            status="Approved",

            expires_at=datetime.utcnow() + timedelta(hours=8),

        )

        DatabaseService.save_permit(permit)

        return permit

    @staticmethod
    def get_all():

        return DatabaseService.get_permits()