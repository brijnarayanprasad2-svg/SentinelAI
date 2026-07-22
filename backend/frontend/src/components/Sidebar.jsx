import {
    FaTachometerAlt,
    FaBell,
    FaExclamationTriangle,
    FaBuilding,
    FaClipboardList,
    FaUsers,
} from "react-icons/fa";

import { NavLink } from "react-router-dom";

const menuItems = [
    {
        name: "Dashboard",
        path: "/",
        icon: <FaTachometerAlt />,
    },
    {
        name: "Alerts",
        path: "/alerts",
        icon: <FaBell />,
    },
    {
        name: "Incidents",
        path: "/incidents",
        icon: <FaExclamationTriangle />,
    },
    {
        name: "Facilities",
        path: "/facilities",
        icon: <FaBuilding />,
    },
    {
        name: "Permits",
        path: "/permits",
        icon: <FaClipboardList />,
    },
    {
        name: "Users",
        path: "/users",
        icon: <FaUsers />,
    },
];

export default function Sidebar() {
    return (
        <aside className="w-72 min-h-screen bg-slate-900 border-r border-slate-800">

            <div className="p-6 border-b border-slate-800">

                <h1 className="text-2xl font-bold text-cyan-400">
                    SentinelAI
                </h1>

                <p className="text-sm text-slate-400 mt-2">
                    Industrial Safety Platform
                </p>

            </div>

            <nav className="p-4">

                {menuItems.map((item) => (
                    <NavLink
                        key={item.name}
                        to={item.path}
                        className={({ isActive }) =>
                            `flex items-center gap-4 p-4 rounded-lg mb-2 transition-all duration-300 ${
                                isActive
                                    ? "bg-cyan-600 text-white"
                                    : "text-slate-300 hover:bg-slate-800"
                            }`
                        }
                    >
                        <span className="text-lg">{item.icon}</span>
                        <span>{item.name}</span>
                    </NavLink>
                ))}

            </nav>

        </aside>
    );
}