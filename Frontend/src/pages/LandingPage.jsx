import React from "react";
import Hero from "../sections/Hero";
import JoinWaitlist from "../sections/JoinWaitlist";
import ReferralCodes from "../sections/ReferralCodes";
import LeaderboardSection from "../sections/LeaderboardSection";
import Footer from "../components/footer";

const LandingPage = () => {
    return (
        <div>
            {/* Hero Section */}
            <Hero />

            {/* Join Waitlist Section */}
            <JoinWaitlist />

            {/* Referral Codes Section */}
            <ReferralCodes />
            <LeaderboardSection />
            <Footer/>
        </div>
    );
};

export default LandingPage;
