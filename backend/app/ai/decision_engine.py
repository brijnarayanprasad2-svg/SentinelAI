from app.engine.risk_engine import RiskEngine


class DecisionEngine:

    @staticmethod
    def analyze(sensor_list):

        risk = RiskEngine.calculate(sensor_list)

        score = risk["risk_score"]

        probability = min(99, score + 10)

        if score >= 80:
            decision = "🚨 Shutdown Plant Immediately"
            emergency = True
            color = "red"

        elif score >= 50:
            decision = "⚠ Reduce Plant Load"
            emergency = False
            color = "orange"

        elif score >= 20:
            decision = "🟡 Inspect Equipment"
            emergency = False
            color = "yellow"

        else:
            decision = "✅ Plant is Safe"
            emergency = False
            color = "green"

        return {

            "risk_score": risk["risk_score"],

            "risk_level": risk["risk_level"],

            "hazards": risk["hazards"],

            "recommendations": risk["recommendations"],

            "generated_at": risk["generated_at"],

            "probability": probability,

            "decision": decision,

            "emergency": emergency,

            "color": color,

        }