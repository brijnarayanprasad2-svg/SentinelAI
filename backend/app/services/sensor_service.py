import random
from datetime import datetime

from app.ai.decision_engine import DecisionEngine
from app.models.sensor import Sensor
from app.services.alert_service import AlertService
from app.services.database_service import DatabaseService
from app.services.incident_service import IncidentService


# ==========================================================
# Industrial Zones
# ==========================================================

ZONES = [
    "Boiler",
    "Storage Tank",
    "Pipeline",
    "Control Room",
    "Loading Area",
]


# ==========================================================
# Sensor Configuration
# ==========================================================

SENSORS = {
    "temperature": {
        "unit": "°C",
        "min": 20,
        "max": 100,
        "critical": 85,
    },
    "pressure": {
        "unit": "bar",
        "min": 1,
        "max": 20,
        "critical": 15,
    },
    "gas": {
        "unit": "ppm",
        "min": 0,
        "max": 100,
        "critical": 70,
    },
    "humidity": {
        "unit": "%",
        "min": 30,
        "max": 80,
        "critical": 70,
    },
    "vibration": {
        "unit": "mm/s",
        "min": 0,
        "max": 10,
        "critical": 7,
    },
}


# ==========================================================
# Sensor Object → Dictionary
# ==========================================================

def sensor_to_dict(sensor: Sensor):
    return {
        "id": sensor.id,
        "sensor_name": sensor.sensor_name,
        "sensor_type": sensor.sensor_type,
        "zone": sensor.zone,
        "value": sensor.value,
        "unit": sensor.unit,
        "status": sensor.status,
        "timestamp": sensor.timestamp.isoformat()
        if sensor.timestamp
        else None,
    }


# ==========================================================
# Generate Live Sensor Data
# ==========================================================

def generate_sensor_data():
    """
    Generate industrial sensor readings.

    Flow
    ----
    Sensor Generation
            ↓
    Save into SQLite
            ↓
    AI Risk Analysis
            ↓
    Alert Generation
            ↓
    Incident Generation
    """

    sensor_list = []

    try:

        # -----------------------------------------
        # Generate Sensor Readings
        # -----------------------------------------

        for sensor_type, config in SENSORS.items():

            value = round(
                random.uniform(
                    config["min"],
                    config["max"],
                ),
                2,
            )

            if value >= config["critical"]:
                status = "Critical"

            elif value >= config["critical"] * 0.80:
                status = "Warning"

            else:
                status = "Normal"

            sensor = Sensor(
                sensor_name=f"{sensor_type.title()} Sensor",
                sensor_type=sensor_type,
                zone=random.choice(ZONES),
                value=value,
                unit=config["unit"],
                status=status,
                timestamp=datetime.utcnow(),
            )

            DatabaseService.save_sensor(sensor)

            sensor_list.append(sensor)

        # -----------------------------------------
        # AI Decision
        # -----------------------------------------

        decision = DecisionEngine.analyze(sensor_list)

        # -----------------------------------------
        # Alert Generation
        # -----------------------------------------

        alerts = AlertService.create_alerts(sensor_list)

        # -----------------------------------------
        # Incident Generation
        # -----------------------------------------

        incident = IncidentService.create_incident(
            decision,
            sensor_list,
        )

        # -----------------------------------------
        # Final Response
        # -----------------------------------------

        return {
            "success": True,
            "generated_at": datetime.utcnow().isoformat(),
            "total_sensors": len(sensor_list),
            "critical_alerts": len(alerts),
            "decision": decision,
            "incident": incident,

            # Simulator uses Sensor Objects
            "sensors": sensor_list,
        }

    except Exception as e:

        print(f"❌ Sensor Service Error: {e}")

        return {
            "success": False,
            "error": str(e),
            "generated_at": datetime.utcnow().isoformat(),
            "sensors": [],
            "critical_alerts": 0,
        }