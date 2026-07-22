import asyncio
from datetime import datetime

from app.services.sensor_service import generate_sensor_data


async def sensor_simulator():
    """
    Background task that continuously generates
    industrial sensor data every 2 seconds.

    Flow:
        Sensor Service
            ↓
        Database
            ↓
        Risk Engine
            ↓
        Decision Engine
            ↓
        Alert Service
            ↓
        Incident Service
    """

    while True:

        try:
            # Generate sensor data
            result = generate_sensor_data()

            # Skip if generation failed
            if not result.get("success", False):
                print(f"❌ Sensor Service Error: {result.get('error')}")
                await asyncio.sleep(2)
                continue

            sensors = result.get("sensors", [])
            decision = result.get("decision", {})
            risk = decision.get("risk", {})

            print("\n" + "=" * 70)
            print(f"📡 LIVE SENSOR DATA   {datetime.now().strftime('%H:%M:%S')}")
            print("=" * 70)

            # -----------------------------
            # Print Sensor Readings
            # -----------------------------
            for sensor in sensors:
                print(
                    f"{sensor.sensor_name:<22}"
                    f"| Zone: {sensor.zone:<15}"
                    f"| Value: {sensor.value:<7} {sensor.unit:<5}"
                    f"| Status: {sensor.status}"
                )

            print("=" * 70)

            # -----------------------------
            # AI Decision Summary
            # -----------------------------
            print(
                f"🎯 Risk Score      : {risk.get('risk_score', 0)}%"
            )

            print(
                f"⚠️  Risk Level     : {risk.get('risk_level', 'LOW')}"
            )

            print(
                f"🤖 AI Decision     : {decision.get('decision', 'No Decision')}"
            )

            print(
                f"📊 Probability     : {decision.get('probability', 0)}%"
            )

            print(
                f"🚨 Emergency       : {'YES' if decision.get('emergency') else 'NO'}"
            )

            print(
                f"🚨 Critical Alerts : {result.get('critical_alerts', 0)}"
            )

            print("=" * 70)

        except Exception as e:
            print(f"❌ Sensor Simulator Error: {e}")

        await asyncio.sleep(2)