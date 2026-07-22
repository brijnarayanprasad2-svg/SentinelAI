import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

export default function MainLayout({ children }) {
    return (
        <div className="flex min-h-screen bg-slate-950 text-white">

            {/* Sidebar */}
            <Sidebar />

            {/* Main Content */}
            <div className="flex flex-col flex-1">

                {/* Top Navbar */}
                <Navbar />

                {/* Page Content */}
                <main className="flex-1 p-8 overflow-auto">
                    {children}
                </main>

            </div>

        </div>
    );
}