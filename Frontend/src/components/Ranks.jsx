import React from "react";

const Ranks = ({ rank, name, profilePicture, score }) => {
  // Determine the background color and border class based on the rank
  const getBackgroundClass = () => {
    if (rank === 1) return "bg-[#67358E]"; // Purple for rank 1
    if (rank === 2) return "bg-green-500"; // Green for rank 2
    return "bg-white border border-gray-800"; // White background with dark gray border
  };

  return (
    <div className={`flex items-center justify-between ${getBackgroundClass()} rounded-full my-2 px-4 py-2 w-full`}>
      {/* Rank Section */}
      <div className="flex items-center gap-4">
        <span className="text-lg font-bold">{rank}</span>

        {/* Profile Picture */}
        <img
          src={profilePicture}
          alt={name}
          className="h-10 w-10 rounded-full"
        />

        {/* Name */}
        <span className={`text-base font-medium ${rank > 2 ? "text-black" : "text-white"}`}>
          {name}
        </span>
      </div>

      {/* Score Section */}
      <div className="flex items-center gap-2">
        <span className={`text-lg ${rank > 2 ? "text-black" : "text-yellow-400"}`}>⭐</span>
        <span className={`text-base font-bold ${rank > 2 ? "text-black" : "text-white"}`}>{score}</span>
      </div>
    </div>
  );
};

export default Ranks;
