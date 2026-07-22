import {
    FaExclamationTriangle,
    FaCheckCircle,
} from "react-icons/fa";

export default function AlertCard({ sensors }) {

    const alerts = sensors.filter(
        (sensor) =>
            sensor.status === "Critical" ||
            sensor.status === "Warning"
    );

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">

            <h2 className="text-2xl font-bold text-white mb-6">
                🚨 Live Alerts
            </h2>

            {alerts.length === 0 ? (

                <div className="flex items-center gap-3 text-green-400">

                    <FaCheckCircle />

                    <span>No active alerts.</span>

                </div>

            ) : (

                alerts.map((sensor, index) => (

                    <div
                        key={index}
                        className="mb-4 p-4 rounded-lg bg-slate-800 border border-slate-700"
                    >

                        <div className="flex justify-between">

                            <div>

                                <h3 className="text-white font-semibold">
                                    {sensor.sensor_name}
                                </h3>

                                <p className="text-gray-400 text-sm">
                                    Zone : {sensor.zone}
                                </p>

                            </div>

                            <div
                                className={
                                    sensor.status === "Critical"
                                        ? "text-red-400"
                                        : "text-yellow-400"
                                }
                            >
                                <FaExclamationTriangle size={22} />
                            </div>

                        </div>

                        <div className="mt-3">

                            <span
                                className={`px-3 py-1 rounded-full text-sm ${
                                    sensor.status === "Critical"
                                        ? "bg-red-600"
                                        : "bg-yellow-500 text-black"
                                }`}
                            >
                                {sensor.status}
                            </span>

                        </div>

                    </div>

                ))

            )}

        </div>

    );

}