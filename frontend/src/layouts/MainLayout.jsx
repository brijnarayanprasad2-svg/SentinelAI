import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

export default function MainLayout({ children }) {
    return (
        <div className="flex min-h-screen bg-slate-950 text-white">

            {/* Sidebar */}
            <Sidebar />

            {/* Main Section */}
            <div className="flex flex-col flex-1 min-w-0">

                {/* Top Navbar */}
                <Navbar />

                {/* Page Content */}
                <main className="flex-1 overflow-y-auto p-6 md:p-8">

                    <div className="max-w-7xl mx-auto">
                        {children}
                    </div>

                </main>

            </div>

        </div>
    );
}