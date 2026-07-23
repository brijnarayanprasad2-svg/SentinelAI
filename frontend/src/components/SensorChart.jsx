import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
    ResponsiveContainer,
} from "recharts";

export default function SensorChart({ sensors }) {

    const data = sensors.map((sensor, index) => ({
        name: index + 1,
        value: sensor.value,
    }));

    return (

        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800 shadow-lg">

            <h2 className="text-xl font-bold text-white mb-6">
                Live Sensor Values
            </h2>

            <ResponsiveContainer width="100%" height={300}>

                <LineChart data={data}>

                    <CartesianGrid strokeDasharray="3 3" stroke="#334155" />

                    <XAxis dataKey="name" stroke="#94a3b8" />

                    <YAxis stroke="#94a3b8" />

                    <Tooltip />

                    <Line
                        type="monotone"
                        dataKey="value"
                        stroke="#06b6d4"
                        strokeWidth={3}
                    />

                </LineChart>

            </ResponsiveContainer>

        </div>

    );

}