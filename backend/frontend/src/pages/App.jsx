import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Alerts from "./pages/Alerts";
import Incidents from "./pages/Incidents";
import Facilities from "./pages/Facilities";
import Permits from "./pages/Permits";
import Users from "./pages/Users";
import Login from "./pages/Login";

function App() {
    return (
        <BrowserRouter>
            <Routes>

                <Route path="/" element={<Dashboard />} />

                <Route path="/alerts" element={<Alerts />} />

                <Route path="/incidents" element={<Incidents />} />

                <Route path="/facilities" element={<Facilities />} />

                <Route path="/permits" element={<Permits />} />

                <Route path="/users" element={<Users />} />

                <Route path="/login" element={<Login />} />

            </Routes>
        </BrowserRouter>
    );
}

export default App;