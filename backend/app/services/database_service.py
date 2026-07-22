from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.database import SessionLocal

from app.models.sensor import Sensor
from app.models.alert import Alert
from app.models.incident import Incident
from app.models.facility import Facility
from app.models.permit import Permit
from app.models.user import User


class DatabaseService:
    """
    ==========================================================
                    SentinelAI Database Service
    ==========================================================

    Centralized service responsible for all database operations.

    Modules:
    • Sensors
    • Alerts
    • Incidents
    • Facilities
    • Permits
    • Users

    ==========================================================
    """

    # ==========================================================
    # DATABASE SESSION
    # ==========================================================

    @staticmethod
    def get_session() -> Session:
        return SessionLocal()

    # ==========================================================
    # SENSOR OPERATIONS
    # ==========================================================

    @staticmethod
    def save_sensor(sensor: Sensor):

        db = DatabaseService.get_session()

        try:
            db.add(sensor)
            db.commit()
            db.refresh(sensor)
            return sensor

        except Exception as e:
            db.rollback()
            print(f"❌ Sensor Save Error: {e}")
            return None

        finally:
            db.close()

    @staticmethod
    def get_latest(limit: int = 20):

        db = DatabaseService.get_session()

        try:

            return (
                db.query(Sensor)
                .order_by(Sensor.id.desc())
                .limit(limit)
                .all()
            )

        except Exception as e:

            print(f"❌ Latest Sensor Fetch Error: {e}")
            return []

        finally:
            db.close()

    @staticmethod
    def get_all():

        db = DatabaseService.get_session()

        try:

            return (
                db.query(Sensor)
                .order_by(Sensor.id.desc())
                .all()
            )

        except Exception as e:

            print(f"❌ Sensor Fetch Error: {e}")
            return []

        finally:
            db.close()

    @staticmethod
    def delete_all_sensors():

        db = DatabaseService.get_session()

        try:

            db.query(Sensor).delete()
            db.commit()

            return True

        except Exception as e:

            db.rollback()
            print(f"❌ Sensor Delete Error: {e}")
            return False

        finally:
            db.close()

    # ==========================================================
    # ALERT OPERATIONS
    # ==========================================================

    @staticmethod
    def save_alert(alert: Alert):

        db = DatabaseService.get_session()

        try:

            db.add(alert)
            db.commit()
            db.refresh(alert)

            return alert

        except Exception as e:

            db.rollback()
            print(f"❌ Alert Save Error: {e}")
            return None

        finally:
            db.close()

    @staticmethod
    def get_alerts(limit: int = 20):

        db = DatabaseService.get_session()

        try:

            return (
                db.query(Alert)
                .order_by(Alert.id.desc())
                .limit(limit)
                .all()
            )

        except Exception as e:

            print(f"❌ Alert Fetch Error: {e}")
            return []

        finally:
            db.close()

    @staticmethod
    def clear_alerts():

        db = DatabaseService.get_session()

        try:

            db.query(Alert).delete()
            db.commit()

            return True

        except Exception as e:

            db.rollback()
            print(f"❌ Alert Delete Error: {e}")
            return False

        finally:
            db.close()
       # ==========================================================
# INCIDENT OPERATIONS
# ==========================================================

    @staticmethod
    def save_incident(incident: Incident):

        db = DatabaseService.get_session()

        try:

            db.add(incident)
            db.commit()
            db.refresh(incident)

            return incident

        except Exception as e:

            db.rollback()
            print(f"❌ Incident Save Error: {e}")
            return None

        finally:

            db.close()

    @staticmethod
    def get_latest_incident():

        db = DatabaseService.get_session()

        try:

            return (
                db.query(Incident)
                .order_by(Incident.id.desc())
                .first()
            )

        except Exception as e:

            print(f"❌ Latest Incident Fetch Error: {e}")
            return None

        finally:

            db.close()

    @staticmethod
    def get_incidents(limit: int = 20):

        db = DatabaseService.get_session()

        try:

            return (
                db.query(Incident)
                .order_by(Incident.id.desc())
                .limit(limit)
                .all()
            )

        except Exception as e:

            print(f"❌ Incident Fetch Error: {e}")
            return []

        finally:

            db.close()

    @staticmethod
    def clear_incidents():

        db = DatabaseService.get_session()

        try:

            db.query(Incident).delete()
            db.commit()

            return True

        except Exception as e:

            db.rollback()
            print(f"❌ Incident Delete Error: {e}")
            return False

        finally:

            db.close()
    # ==========================================================
    # PERMIT OPERATIONS
    # ==========================================================

    @staticmethod
    def save_permit(permit: Permit):

        db = DatabaseService.get_session()

        try:
            db.add(permit)
            db.commit()
            db.refresh(permit)
            return permit

        except Exception as e:
            db.rollback()
            print(f"❌ Permit Save Error: {e}")
            return None

        finally:
            db.close()

    @staticmethod
    def get_permits(limit: int = 20):

        db = DatabaseService.get_session()

        try:
            return (
                db.query(Permit)
                .order_by(Permit.id.desc())
                .limit(limit)
                .all()
            )

        except Exception as e:
            print(f"❌ Permit Fetch Error: {e}")
            return []

        finally:
            db.close()

    # ==========================================================
    # USER OPERATIONS
    # ==========================================================

    @staticmethod
    def save_user(user: User):

        db = DatabaseService.get_session()

        try:
            db.add(user)
            db.commit()
            db.refresh(user)
            return user

        except Exception as e:
            db.rollback()
            print(f"❌ User Save Error: {e}")
            return None

        finally:
            db.close()

    @staticmethod
    def get_user_by_email(email: str):

        db = DatabaseService.get_session()

        try:
            return (
                db.query(User)
                .filter(User.email == email)
                .first()
            )

        except Exception as e:
            print(f"❌ User Fetch Error: {e}")
            return None

        finally:
            db.close()

    @staticmethod
    def get_all_users():

        db = DatabaseService.get_session()

        try:
            return (
                db.query(User)
                .order_by(User.id.desc())
                .all()
            )

        except Exception as e:
            print(f"❌ Users Fetch Error: {e}")
            return []

        finally:
            db.close()

    # ==========================================================
    # FACILITY OPERATIONS
    # ==========================================================

    @staticmethod
    def save_facility(facility: Facility):

        db = DatabaseService.get_session()

        try:
            db.add(facility)
            db.commit()
            db.refresh(facility)
            return facility

        except Exception as e:
            db.rollback()
            print(f"❌ Facility Save Error: {e}")
            return None

        finally:
            db.close()

    @staticmethod
    def get_facilities():

        db = DatabaseService.get_session()

        try:
            return (
                db.query(Facility)
                .order_by(Facility.id.desc())
                .all()
            )

        except Exception as e:
            print(f"❌ Facility Fetch Error: {e}")
            return []

        finally:
            db.close()
                # ==========================================================
    # DASHBOARD ANALYTICS
    # ==========================================================

    @staticmethod
    def sensor_count():

        db = DatabaseService.get_session()

        try:
            return db.query(Sensor).count()

        finally:
            db.close()

    @staticmethod
    def alert_count():

        db = DatabaseService.get_session()

        try:
            return db.query(Alert).count()

        finally:
            db.close()

    @staticmethod
    def incident_count():

        db = DatabaseService.get_session()

        try:
            return db.query(Incident).count()

        finally:
            db.close()

    @staticmethod
    def permit_count():

        db = DatabaseService.get_session()

        try:
            return db.query(Permit).count()

        finally:
            db.close()

    @staticmethod
    def facility_count():

        db = DatabaseService.get_session()

        try:
            return db.query(Facility).count()

        finally:
            db.close()

    @staticmethod
    def user_count():

        db = DatabaseService.get_session()

        try:
            return db.query(User).count()

        finally:
            db.close()

    # ==========================================================
    # DASHBOARD SUMMARY
    # ==========================================================

    @staticmethod
    def dashboard_summary():

        return {
            "total_sensors": DatabaseService.sensor_count(),
            "total_alerts": DatabaseService.alert_count(),
            "total_incidents": DatabaseService.incident_count(),
            "total_permits": DatabaseService.permit_count(),
            "total_facilities": DatabaseService.facility_count(),
            "total_users": DatabaseService.user_count(),
        }

    # ==========================================================
    # DATABASE HEALTH CHECK
    # ==========================================================

    @staticmethod
    def check_connection():

        db = DatabaseService.get_session()

        try:
            db.execute(text("SELECT 1"))
            return True

        except Exception as e:
            print(f"❌ Database Connection Error: {e}")
            return False

        finally:
            db.close()

    # ==========================================================
    # RESET DATABASE (Development Only)
    # ==========================================================

    @staticmethod
    def clear_database():

        db = DatabaseService.get_session()

        try:

            db.query(Alert).delete()
            db.query(Incident).delete()
            db.query(Sensor).delete()
            db.query(Permit).delete()
            db.query(Facility).delete()

            db.commit()

            return True

        except Exception as e:

            db.rollback()

            print(f"❌ Database Clear Error: {e}")

            return False

        finally:
            db.close()

    # ==========================================================
    # DATABASE INFORMATION
    # ==========================================================

    @staticmethod
    def database_info():

        return {
            "connected": DatabaseService.check_connection(),
            "database": "SQLite",
            "tables": [
                "Sensors",
                "Alerts",
                "Incidents",
                "Facilities",
                "Permits",
                "Users",
            ],
            "statistics": DatabaseService.dashboard_summary(),
        }
            