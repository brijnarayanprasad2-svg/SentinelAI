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
                <h2 className="text-2xl font-bold text-white flex items-center gap-3">
                    <FaBrain className="text-cyan-400" />
                    AI Decision Engine
                </h2>

                <p className="text-gray-400 mt-4">
                    Waiting for AI analysis...
                </p>
            </div>
        );
    }

    // Backend se direct values aa rahi hain
    const risk = decision;

    let color = "text-green-400";
    let bg = "bg-green-500/20";

    switch (risk.risk_level) {

        case "MEDIUM":
            color = "text-yellow-400";
            bg = "bg-yellow-500/20";
            break;

        case "HIGH":
            color = "text-orange-400";
            bg = "bg-orange-500/20";
            break;

        case "EXTREME":
        case "CRITICAL":
            color = "text-red-400";
            bg = "bg-red-500/20";
            break;

        default:
            color = "text-green-400";
            bg = "bg-green-500/20";
    }

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">

            <div className="flex items-center gap-3 mb-6">

                <FaBrain className="text-cyan-400 text-3xl" />

                <h2 className="text-2xl font-bold text-white">
                    AI Decision Engine
                </h2>

            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

                {/* Risk Level */}

                <div className={`${bg} rounded-xl p-5`}>

                    <div className="flex items-center gap-2 mb-2">

                        <FaShieldAlt className={color} />

                        <span className="text-gray-300">
                            Risk Level
                        </span>

                    </div>

                    <h2 className={`text-3xl font-bold ${color}`}>
                        {risk.risk_level}
                    </h2>

                </div>

                {/* Risk Score */}

                <div className={`${bg} rounded-xl p-5`}>

                    <div className="flex items-center gap-2 mb-2">

                        <FaExclamationTriangle className={color} />

                        <span className="text-gray-300">
                            Risk Score
                        </span>

                    </div>

                    <h2 className={`text-3xl font-bold ${color}`}>
                        {risk.risk_score}%
                    </h2>

                </div>

                {/* Probability */}

                <div className={`${bg} rounded-xl p-5`}>

                    <div className="flex items-center gap-2 mb-2">

                        <FaCheckCircle className={color} />

                        <span className="text-gray-300">
                            Probability
                        </span>

                    </div>

                    <h2 className={`text-3xl font-bold ${color}`}>
                        {risk.probability}%
                    </h2>

                </div>

            </div>

            {/* AI Decision */}

           <div className="mt-8 p-5 rounded-xl bg-slate-800">

    <h2 className="text-xl font-bold text-white mb-3">
        🤖 AI Recommendation
    </h2>

    <p className={`${color} text-lg font-bold mb-4`}>
        {decision.decision}
    </p>

    <h3 className="text-white font-semibold mb-2">
        Recommended Actions
    </h3>

    <ul className="space-y-2">

        {decision.recommendations?.map((item, index) => (

            <li
                key={index}
                className="flex items-center gap-2 text-gray-300"
            >
                ✅ {item}
            </li>

        ))}

    </ul>

</div>

        </div>

    );
}