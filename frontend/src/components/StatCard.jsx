import {
    FaMicrochip,
    FaExclamationTriangle,
    FaShieldAlt,
    FaIndustry,
} from "react-icons/fa";

export default function StatCard({
    title,
    value,
    color = "cyan",
    type = "sensor",
}) {

    const colors = {
        cyan: "text-cyan-400 border-cyan-500",
        red: "text-red-400 border-red-500",
        green: "text-green-400 border-green-500",
        yellow: "text-yellow-400 border-yellow-500",
    };

    const icons = {
        sensor: <FaMicrochip size={28} />,
        alert: <FaExclamationTriangle size={28} />,
        risk: <FaShieldAlt size={28} />,
        plant: <FaIndustry size={28} />,
    };

    return (
        <div className={`bg-slate-900 border ${colors[color].split(" ")[1]} rounded-2xl p-6 shadow-lg hover:scale-105 transition-all duration-300`}>

            <div className="flex justify-between items-center">

                <div>

                    <p className="text-slate-400 text-sm">
                        {title}
                    </p>

                    <h2 className={`text-4xl font-bold mt-3 ${colors[color].split(" ")[0]}`}>
                        {value}
                    </h2>

                </div>

                <div className={colors[color].split(" ")[0]}>
                    {icons[type]}
                </div>

            </div>

        </div>
    );
}