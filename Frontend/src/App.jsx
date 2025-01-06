import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar"; // Navbar component
import Footer from "./components/Footer";
import LandingPage from "./pages/LandingPage"; // Landing page with Hero section //import Leaderboard from "./pages/Leaderboard";
//import SignupForm from "./pages/SignupForm";
import SignupPage from "./pages/SignupPage"
import WelcomeAboard from "./pages/WelcomeAbroad";
const App = () => {
    return (
        <Router>
            <div>
                {/* Navbar will always be visible */}
                <Navbar />
                {/* Routes for different pages */}
                <Routes>
                    <Route path="/" element={<LandingPage />} />
                    <Route path="/signup" element={<SignupPage/>} />
                    <Route path="/welcome" element ={<WelcomeAboard/>}/>
                </Routes>
                <Footer/>
            </div>
        </Router>
    );
};

export default App;
