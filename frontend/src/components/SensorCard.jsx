import {
    FaTemperatureHigh,
    FaTachometerAlt,
    FaWind,
    FaTint,
    FaCogs,
    FaMapMarkerAlt,
} from "react-icons/fa";

export default function SensorCard({
    title,
    value,
    unit,
    zone,
    status,
}) {

    // -----------------------------
    // Status Color
    // -----------------------------

    const statusColor =
        status === "Critical"
            ? "bg-red-500"
            : status === "Warning"
            ? "bg-yellow-500 text-black"
            : "bg-green-500";

    // -----------------------------
    // Sensor Icon
    // -----------------------------

    let icon = <FaCogs className="text-cyan-400 text-3xl" />;

    if (title.toLowerCase().includes("temperature"))
        icon = <FaTemperatureHigh className="text-red-400 text-3xl" />;

    else if (title.toLowerCase().includes("pressure"))
        icon = <FaTachometerAlt className="text-orange-400 text-3xl" />;

    else if (title.toLowerCase().includes("gas"))
        icon = <FaWind className="text-green-400 text-3xl" />;

    else if (title.toLowerCase().includes("humidity"))
        icon = <FaTint className="text-blue-400 text-3xl" />;

    else if (title.toLowerCase().includes("vibration"))
        icon = <FaCogs className="text-purple-400 text-3xl" />;

    return (
        <div className="bg-slate-900 border border-slate-800 rounded-2xl shadow-lg p-6 transition-all duration-300 hover:scale-105 hover:border-cyan-500 hover:shadow-cyan-500/20">

            {/* Header */}

            <div className="flex justify-between items-center mb-5">

                <div className="flex items-center gap-3">

                    {icon}

                    <h2 className="text-lg font-semibold text-white">
                        {title}
                    </h2>

                </div>

                <span
                    className={`px-3 py-1 rounded-full text-xs font-bold text-white ${statusColor}`}
                >
                    {status}
                </span>

            </div>

            {/* Sensor Value */}

            <div className="mb-5">

                <h1 className="text-5xl font-bold text-cyan-400">

                    {value}

                    <span className="text-xl ml-2 text-gray-300">
                        {unit}
                    </span>

                </h1>

            </div>

            {/* Zone */}

            <div className="flex items-center text-gray-400">

                <FaMapMarkerAlt className="mr-2" />

                <span>{zone}</span>

            </div>

        </div>
    );
}