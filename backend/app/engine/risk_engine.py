from datetime import datetime

from app.models.sensor import Sensor


class RiskEngine:

    @staticmethod
    def calculate(sensor_list):

        risk_score = 0
        hazards = []
        recommendations = []

        sensor_status = {}

        # -----------------------------
        # Individual Sensor Analysis
        # -----------------------------
        for sensor in sensor_list:

            sensor_status[sensor.sensor_type] = sensor.status

            if sensor.status == "Critical":

                risk_score += 20

                hazards.append(
                    f"{sensor.sensor_name} is Critical in {sensor.zone}"
                )

                if sensor.sensor_type == "temperature":
                    recommendations.append(
                        "Stop all hot work immediately."
                    )

                elif sensor.sensor_type == "gas":
                    recommendations.append(
                        "Evacuate the affected area."
                    )

                elif sensor.sensor_type == "pressure":
                    recommendations.append(
                        "Inspect pressure relief valve."
                    )

                elif sensor.sensor_type == "humidity":
                    recommendations.append(
                        "Check ventilation system."
                    )

                elif sensor.sensor_type == "vibration":
                    recommendations.append(
                        "Shutdown machine for inspection."
                    )

            elif sensor.status == "Warning":

                risk_score += 10

                hazards.append(
                    f"{sensor.sensor_name} is Warning"
                )

        # ====================================
        # Compound Risk Detection
        # ====================================

        # Fire Risk
        if (
            sensor_status.get("temperature") == "Critical"
            and sensor_status.get("gas") == "Critical"
        ):

            risk_score += 25

            hazards.append("🔥 Fire Risk Detected")

            recommendations.append(
                "Activate Fire Suppression System."
            )

        # Explosion Risk
        if (
            sensor_status.get("temperature") == "Critical"
            and sensor_status.get("pressure") == "Critical"
            and sensor_status.get("gas") == "Critical"
        ):

            risk_score += 40

            hazards.append("💥 Explosion Risk")

            recommendations.append(
                "Emergency Plant Shutdown Required."
            )

        # Machine Failure
        if (
            sensor_status.get("pressure") == "Critical"
            and sensor_status.get("vibration") == "Critical"
        ):

            risk_score += 20

            hazards.append("⚙ Machine Failure Risk")

            recommendations.append(
                "Inspect Rotating Equipment Immediately."
            )

        # Moisture Damage
        if (
            sensor_status.get("humidity") == "Critical"
            and sensor_status.get("temperature") == "Critical"
        ):

            risk_score += 15

            hazards.append("💧 Moisture Damage Risk")

            recommendations.append(
                "Improve Ventilation."
            )

        # -----------------------------
        # Risk Level
        # -----------------------------

        risk_score = min(risk_score, 100)

        if risk_score >= 80:
            level = "EXTREME"

        elif risk_score >= 60:
            level = "HIGH"

        elif risk_score >= 30:
            level = "MEDIUM"

        else:
            level = "LOW"

        return {

            "risk_score": risk_score,

            "risk_level": level,

            "hazards": list(set(hazards)),

            "recommendations": list(set(recommendations)),

            "generated_at": datetime.utcnow()
        }