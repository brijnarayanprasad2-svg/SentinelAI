from app.models.alert import Alert
from app.services.database_service import DatabaseService


class AlertService:
    """
    Handles automatic alert generation
    based on critical sensor readings.
    """

    # =====================================================
    # Generate Alerts
    # =====================================================
    @staticmethod
    def create_alerts(sensor_list):

        alerts_created = []

        recommendations = {
            "temperature": "Stop all hot work immediately.",
            "pressure": "Inspect pressure relief valve.",
            "gas": "Evacuate affected area immediately.",
            "humidity": "Check ventilation system.",
            "vibration": "Shutdown machine for inspection.",
        }

        for sensor in sensor_list:

            # Ignore non-critical sensors
            if sensor.status != "Critical":
                continue

            alert = Alert(
                title=f"{sensor.sensor_name} Critical",
                zone=sensor.zone,
                severity="Critical",
                status="Open",
                recommendation=recommendations.get(
                    sensor.sensor_type,
                    "Inspect equipment immediately.",
                ),
            )

            saved_alert = DatabaseService.save_alert(alert)

            if saved_alert:
                alerts_created.append(saved_alert)

        return alerts_created