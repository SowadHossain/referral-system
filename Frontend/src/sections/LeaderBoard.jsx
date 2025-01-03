import React from "react";
import Ranks from "../components/Ranks"

const LeaderBoard = () => {
  const data = [
    { rank: 1, name: "Christy Obinna", profilePicture: "https://via.placeholder.com/150", score: 127 },
    { rank: 2, name: "Jane Ubani", profilePicture: "https://via.placeholder.com/150", score: 92 },
    { rank: 3, name: "Owen Gbenga", profilePicture: "https://via.placeholder.com/150", score: 84 },
    { rank: 4, name: "Chidi M. Uwakwe", profilePicture: "https://via.placeholder.com/150", score: 72 },
    { rank: 5, name: "Femi Adeleke", profilePicture: "https://via.placeholder.com/150", score: 70 },
    { rank: 6, name: "Umar Yusuf", profilePicture: "https://via.placeholder.com/150", score: 65 },
    { rank: 7, name: "Brenda Bassey", profilePicture: "https://via.placeholder.com/150", score: 51 },
  ];

  return (
    <div className="bg-gradient-to-b from-white-100 to-white-200 p-8 rounded-2xl shadow-lg max-w-4xl mx-auto mb-8 w-4/5">
      {/* Title */}
      <h1 className="text-2xl font-bold text-center text-black mb-6">
        See Who's Referring the Most
      </h1>

      {/* Leaderboard */}
      <div className="space-y-4">
        {data.map((person) => (
          <Ranks
            key={person.rank}
            rank={person.rank}
            name={person.name}
            profilePicture={person.profilePicture}
            score={person.score}
          />
        ))}
      </div>
    </div>
  );
};

export default LeaderBoard;
