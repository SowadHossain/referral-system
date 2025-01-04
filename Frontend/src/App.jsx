import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar"; // Navbar component
import Footer from "./components/Footer";
import LandingPage from "./pages/LandingPage";
import SignupPage from "./pages/SignupPage"
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
                
                </Routes>
                <Footer/>
            </div>
        </Router>
    );
};

export default App;
