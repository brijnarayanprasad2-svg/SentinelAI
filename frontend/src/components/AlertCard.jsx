import {
    FaExclamationTriangle,
    FaCheckCircle,
    FaMapMarkerAlt,
    FaMicrochip,
} from "react-icons/fa";

export default function AlertCard({ sensors }) {

    const alerts = sensors.filter(
        (sensor) =>
            sensor.status === "Critical" ||
            sensor.status === "Warning"
    );

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">

            <div className="flex items-center justify-between mb-6">

                <h2 className="text-2xl font-bold text-white">
                    🚨 Live Alerts
                </h2>

                <span className="px-3 py-1 rounded-full bg-red-600 text-white text-sm font-semibold">
                    {alerts.length} Active
                </span>

            </div>

            {alerts.length === 0 ? (

                <div className="flex items-center gap-3 text-green-400 text-lg">

                    <FaCheckCircle size={22} />

                    <span>No active alerts.</span>

                </div>

            ) : (

                alerts.map((sensor) => (

                    <div
                        key={sensor.id}
                        className="mb-5 p-5 rounded-xl bg-slate-800 border border-slate-700 hover:border-cyan-500 transition-all duration-300 hover:shadow-lg hover:shadow-cyan-500/20"
                    >

                        {/* Header */}

                        <div className="flex justify-between items-start">

                            <div>

                                <div className="flex items-center gap-2">

                                    <FaMicrochip className="text-cyan-400" />

                                    <h3 className="text-lg font-bold text-white">
                                        {sensor.sensor_name}
                                    </h3>

                                </div>

                                <div className="flex items-center gap-2 mt-2 text-gray-400 text-sm">

                                    <FaMapMarkerAlt />

                                    <span>{sensor.zone}</span>

                                </div>

                            </div>

                            <FaExclamationTriangle
                                size={24}
                                className={
                                    sensor.status === "Critical"
                                        ? "text-red-500"
                                        : "text-yellow-400"
                                }
                            />

                        </div>

                        {/* Sensor Value */}

                        <div className="mt-4">

                            <p className="text-gray-400 text-sm">
                                Current Reading
                            </p>

                            <h2 className="text-2xl font-bold text-cyan-400">

                                {sensor.value}

                                <span className="text-base text-gray-300 ml-2">
                                    {sensor.unit}
                                </span>

                            </h2>

                        </div>

                        {/* Status */}

                        <div className="mt-4 flex items-center justify-between">

                            <span
                                className={`px-4 py-2 rounded-full font-semibold ${
                                    sensor.status === "Critical"
                                        ? "bg-red-600 text-white"
                                        : "bg-yellow-400 text-black"
                                }`}
                            >
                                {sensor.status}
                            </span>

                        </div>

                        {/* AI Recommendation */}

                        <div className="mt-5 border-t border-slate-700 pt-4">

                            <h4 className="text-cyan-400 font-semibold mb-2">
                                🤖 AI Recommendation
                            </h4>

                            <p className="text-gray-300 text-sm leading-6">

                                {sensor.status === "Critical"
                                    ? "Immediately stop the affected equipment, inspect the area, and notify the safety team."
                                    : "Monitor this sensor closely and schedule maintenance if values continue increasing."}

                            </p>

                        </div>

                    </div>

                ))

            )}

        </div>

    );

}