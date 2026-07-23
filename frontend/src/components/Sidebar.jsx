import {
    FaTachometerAlt,
    FaBell,
    FaExclamationTriangle,
    FaBuilding,
    FaClipboardList,
    FaUsers,
    FaCircle,
    FaShieldAlt,
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

        <aside className="w-72 min-h-screen bg-slate-900 border-r border-slate-800 flex flex-col">

            {/* Logo */}

            <div className="p-6 border-b border-slate-800">

                <div className="flex items-center gap-3">

                    <FaShieldAlt className="text-cyan-400 text-3xl" />

                    <div>

                        <h1 className="text-2xl font-bold text-cyan-400">
                            SentinelAI
                        </h1>

                        <p className="text-xs text-slate-400">
                            Industrial Safety Platform
                        </p>

                    </div>

                </div>

            </div>

            {/* Menu */}

            <nav className="flex-1 p-4">

                {menuItems.map((item) => (

                    <NavLink
                        key={item.name}
                        to={item.path}
                        className={({ isActive }) =>
                            `flex items-center gap-4 p-4 rounded-xl mb-3 transition-all duration-300 ${
                                isActive
                                    ? "bg-cyan-600 text-white shadow-lg"
                                    : "text-slate-300 hover:bg-slate-800 hover:text-cyan-400"
                            }`
                        }
                    >
                        <span className="text-lg">
                            {item.icon}
                        </span>

                        <span className="font-medium">
                            {item.name}
                        </span>

                    </NavLink>

                ))}

            </nav>

            {/* Footer */}

            <div className="border-t border-slate-800 p-5">

                <div className="flex items-center gap-2 mb-3">

                    <FaCircle className="text-green-500 text-xs animate-pulse" />

                    <span className="text-green-400 text-sm font-medium">
                        Backend Connected
                    </span>

                </div>

                <p className="text-xs text-slate-500">
                    SentinelAI v1.0
                </p>

                <p className="text-xs text-slate-600 mt-1">
                    AI Powered Monitoring
                </p>

            </div>

        </aside>

    );

}