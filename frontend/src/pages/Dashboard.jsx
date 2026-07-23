import { useEffect, useState } from "react";
import api from "../api/api";

import MainLayout from "../layouts/MainLayout";

import SensorCard from "../components/SensorCard";
import StatCard from "../components/StatCard";
import SensorChart from "../components/SensorChart";
import AIDecisionPanel from "../components/AIDecisionPanel";
import AlertCard from "../components/AlertCard";

export default function Dashboard() {

    const [sensors, setSensors] = useState([]);
    const [decision, setDecision] = useState(null);

    async function loadSensors() {

        try {

            const res = await api.get("/api/sensors/latest");

            console.log("API Response:", res.data);

            if (res.data.success) {
                setSensors(res.data.sensors || []);
                setDecision(res.data.decision || null);
            }

        } catch (err) {

            console.error(err);

        }

    }

    useEffect(() => {

        loadSensors();

        const interval = setInterval(loadSensors, 2000);

        return () => clearInterval(interval);

    }, []);

    const criticalSensors = sensors.filter(
        sensor => sensor.status === "Critical"
    ).length;

    const warningSensors = sensors.filter(
        sensor => sensor.status === "Warning"
    ).length;

    const plantStatus =
        criticalSensors > 0 ? "ALERT" : "SAFE";

    return (

        <MainLayout>

            <h1 className="text-4xl font-bold text-white mb-8">
                Industrial Monitoring Dashboard
            </h1>

            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 mb-8">

                <StatCard
                    title="Total Sensors"
                    value={sensors.length}
                    color="cyan"
                    type="sensor"
                />

                <StatCard
                    title="Critical Sensors"
                    value={criticalSensors}
                    color="red"
                    type="alert"
                />

                <StatCard
                    title="Warnings"
                    value={warningSensors}
                    color="yellow"
                    type="risk"
                />

                <StatCard
                    title="Plant Status"
                    value={plantStatus}
                    color={plantStatus === "SAFE" ? "green" : "red"}
                    type="plant"
                />

            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

                {sensors.map(sensor => (

                    <SensorCard
                        key={sensor.id}
                        title={sensor.sensor_name}
                        value={sensor.value}
                        unit={sensor.unit}
                        zone={sensor.zone}
                        status={sensor.status}
                    />

                ))}

            </div>

            <div className="mt-10">
                <SensorChart sensors={sensors} />
            </div>

            <div className="mt-10">
                <AIDecisionPanel decision={decision} />
            </div>

            <div className="mt-10">
                <AlertCard sensors={sensors} />
            </div>

        </MainLayout>

    );

}