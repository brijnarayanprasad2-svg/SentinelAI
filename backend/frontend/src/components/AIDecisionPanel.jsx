import {
    FaBrain,
    FaShieldAlt,
    FaExclamationTriangle,
    FaCheckCircle,
} from "react-icons/fa";

export default function AIDecisionPanel({ decision }) {

    if (!decision) {

        return (

            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">

                <h2 className="text-2xl text-white font-bold">
                    🤖 AI Decision Engine
                </h2>

                <p className="text-gray-400 mt-4">
                    Waiting for AI analysis...
                </p>

            </div>

        );

    }

    const risk = decision.risk;

    let color = "text-green-400";
    let bg = "bg-green-500/20";

    if (risk.risk_level === "MEDIUM") {
        color = "text-yellow-400";
        bg = "bg-yellow-500/20";
    }

    if (risk.risk_level === "HIGH") {
        color = "text-orange-400";
        bg = "bg-orange-500/20";
    }

    if (risk.risk_level === "EXTREME") {
        color = "text-red-400";
        bg = "bg-red-500/20";
    }

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">

            <div className="flex items-center gap-3 mb-6">

                <FaBrain className="text-cyan-400 text-3xl"/>

                <h2 className="text-2xl font-bold text-white">
                    AI Decision Engine
                </h2>

            </div>

            <div className="grid md:grid-cols-3 gap-6">

                <div className={`${bg} rounded-xl p-5`}>

                    <div className="flex items-center gap-2 mb-2">

                        <FaShieldAlt className={color}/>

                        <span className="text-gray-300">
                            Risk Level
                        </span>

                    </div>

                    <h2 className={`text-3xl font-bold ${color}`}>
                        {risk.risk_level}
                    </h2>

                </div>

                <div className={`${bg} rounded-xl p-5`}>

                    <div className="flex items-center gap-2 mb-2">

                        <FaExclamationTriangle className={color}/>

                        <span className="text-gray-300">
                            Risk Score
                        </span>

                    </div>

                    <h2 className={`text-3xl font-bold ${color}`}>
                        {risk.risk_score}%
                    </h2>

                </div>

                <div className={`${bg} rounded-xl p-5`}>

                    <div className="flex items-center gap-2 mb-2">

                        <FaCheckCircle className={color}/>

                        <span className="text-gray-300">
                            Probability
                        </span>

                    </div>

                    <h2 className={`text-3xl font-bold ${color}`}>
                        {decision.probability}%
                    </h2>

                </div>

            </div>

            <div className="mt-8 p-5 rounded-xl bg-slate-800">

                <h2 className="text-xl font-bold text-white mb-2">
                    AI Decision
                </h2>

                <p className={`${color} text-lg font-semibold`}>
                    {decision.decision}
                </p>

            </div>

        </div>

    );

}