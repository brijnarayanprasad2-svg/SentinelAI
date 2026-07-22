import { FaBell, FaUserCircle } from "react-icons/fa";

export default function Navbar() {

    const currentDate = new Date().toLocaleString();

    return (
        <header className="flex justify-between items-center px-8 py-5 bg-slate-900 border-b border-slate-800">

            {/* Left */}
            <div>
                <h2 className="text-2xl font-bold text-white">
                    Industrial Safety Dashboard
                </h2>

                <p className="text-sm text-slate-400">
                    {currentDate}
                </p>
            </div>

            {/* Right */}
            <div className="flex items-center gap-6">

                <button className="relative text-xl text-slate-300 hover:text-cyan-400 transition">

                    <FaBell />

                    <span className="absolute -top-2 -right-2 w-5 h-5 rounded-full bg-red-500 text-xs flex items-center justify-center">
                        3
                    </span>

                </button>

                <div className="flex items-center gap-3">

                    <FaUserCircle
                        size={36}
                        className="text-cyan-400"
                    />

                    <div>

                        <h3 className="font-semibold">
                            Admin
                        </h3>

                        <p className="text-xs text-slate-400">
                            System Operator
                        </p>

                    </div>

                </div>

            </div>

        </header>
    );
}