from app.services.database_service import DatabaseService


class DashboardService:

    @staticmethod
    def get_dashboard():

        sensors = DatabaseService.get_latest(20)
        alerts = DatabaseService.get_alerts(20)

        total = len(sensors)

        normal = sum(1 for s in sensors if s.status == "Normal")
        warning = sum(1 for s in sensors if s.status == "Warning")
        critical = sum(1 for s in sensors if s.status == "Critical")

        return {
            "total_sensors": total,
            "normal": normal,
            "warning": warning,
            "critical": critical,
            "total_alerts": len(alerts),
            "latest_sensors": sensors,
            "latest_alerts": alerts,
        }