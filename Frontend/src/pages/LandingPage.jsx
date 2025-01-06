import React from "react";
import Hero from "../sections/Hero";
import JoinWaitlist from "../sections/JoinWaitlist";
import ReferralCodes from "../sections/ReferralCodes";
import LeaderboardSection from "../sections/LeaderboardSection";
import LeaderBoard from "../sections/LeaderBoard";
import { useRef } from "react";
import Navbar from "../components/Navbar";

const LandingPage = () => {
    const leaderboardRef = useRef(null);
    const detailsRef = useRef(null);
    return (
        <div>
            <Navbar leaderboardRef={leaderboardRef} />
            {/* Hero Section */}
            <Hero DetailsRef={detailsRef} />

            {/* Join Waitlist Section */}
            <div ref={detailsRef} >
                <JoinWaitlist />
            </div>
            {/* Referral Codes Section */}

            <ReferralCodes />


            <LeaderboardSection />

            <div ref={leaderboardRef}>
                <LeaderBoard />
            </div>
        </div>
    );
};

export default LandingPage;
