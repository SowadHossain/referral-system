import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar"; // Navbar component
import LandingPage from "./pages/LandingPage"; // Landing page with Hero section //import Leaderboard from "./pages/Leaderboard";
//import SignupForm from "./pages/SignupForm";
const App = () => {
    return (
        <Router>
            <div>
                {/* Navbar will always be visible */}
                <Navbar />

                {/* Routes for different pages */}
                <Routes>
                    <Route path="/" element={<LandingPage />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
