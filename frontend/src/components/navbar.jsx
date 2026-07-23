import {
    FaBell,
    FaUserCircle,
    FaCircle,
    FaClock,
} from "react-icons/fa";

export default function Navbar() {

    const currentDate = new Date().toLocaleString();

    return (

        <header className="flex justify-between items-center px-8 py-5 bg-slate-900 border-b border-slate-800 shadow-lg">

            {/* Left */}

            <div>

                <h2 className="text-3xl font-bold text-white">
                    Industrial Safety Dashboard
                </h2>

                <div className="flex items-center gap-5 mt-2">

                    <div className="flex items-center gap-2">

                        <FaCircle className="text-green-500 animate-pulse text-xs" />

                        <span className="text-green-400 text-sm font-medium">
                            Live Monitoring Active
                        </span>

                    </div>

                    <div className="flex items-center gap-2 text-slate-400 text-sm">

                        <FaClock />

                        <span>{currentDate}</span>

                    </div>

                </div>

            </div>

            {/* Right */}

            <div className="flex items-center gap-8">

                {/* Notification */}

                <button className="relative text-2xl text-slate-300 hover:text-cyan-400 transition">

                    <FaBell />

                    <span className="absolute -top-2 -right-2 w-6 h-6 rounded-full bg-red-600 text-white text-xs flex items-center justify-center font-bold">
                        3
                    </span>

                </button>

                {/* User */}

                <div className="flex items-center gap-3">

                    <FaUserCircle
                        size={42}
                        className="text-cyan-400"
                    />

                    <div>

                        <h3 className="font-bold text-white">
                            Admin
                        </h3>

                        <p className="text-xs text-slate-400">
                            Industrial Safety Operator
                        </p>

                    </div>

                </div>

            </div>

        </header>

    );

}