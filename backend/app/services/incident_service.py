from app.models.incident import Incident
from app.services.database_service import DatabaseService


class IncidentService:
    """
    Creates industrial incidents based on AI decision.
    """

    @staticmethod
    def create_incident(decision, sensor_list):

        risk_level = decision["risk_level"]

        # Incident only for serious risks
        if risk_level not in ["HIGH", "EXTREME"]:
            return None

        incident = Incident(

            title=f"{risk_level} Risk Detected",

            description=f"AI detected {risk_level} industrial risk.",

            zone=sensor_list[0].zone if sensor_list else "Unknown",

            severity=risk_level,

            status="Open",

        )

        DatabaseService.save_incident(incident)

        return incident