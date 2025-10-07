import { useState } from "react";

export default function Meet() {
  const [userLocation, setUserLocation] = useState("");
  const [friendLocation, setFriendLocation] = useState("");
  const [mode, setMode] = useState("drive");

  const handleFindMidpoint = () => {
    if (!userLocation || !friendLocation) {
      alert("Please enter both locations!");
      return;
    }

    // Placeholder for now
    console.log("Finding midpoint between:", userLocation, friendLocation, "via", mode);
    alert(`Finding midpoint between:\n${userLocation} and ${friendLocation}\nMode: ${mode}`);
  };

  return (
    <div className="mt-24 px-6 flex flex-col items-center">
      <h2 className="text-3xl font-bold mb-8 text-center">Plan Your Meetup</h2>

      <div className="w-full max-w-xl bg-white rounded-2xl shadow-md p-6 space-y-6 border border-gray-100">
        {/* Departure Input */}
        <div>
          <label className="block text-gray-700 font-semibold mb-2">
            Your Departure:
          </label>
          <input
            type="text"
            value={userLocation}
            onChange={(e) => setUserLocation(e.target.value)}
            placeholder="Enter your address or city..."
            className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 outline-none"
          />
        </div>

        {/* Transport Mode Selector */}
        <div>
          <label className="block text-gray-700 font-semibold mb-2">
            Mode of Transport:
          </label>
          <select
            value={mode}
            onChange={(e) => setMode(e.target.value)}
            className="w-full px-4 py-3 border border-gray-300 rounded-xl bg-white focus:ring-2 focus:ring-blue-500 outline-none"
          >
            <option value="drive">Drive 🚗</option>
            <option value="walk">Walk 🚶‍♀️</option>
            <option value="bike">Bike 🚴</option>
            <option value="transit">Transit 🚆</option>
          </select>
        </div>

        {/* Destination Input */}
        <div>
          <label className="block text-gray-700 font-semibold mb-2">
            Friend's Location:
          </label>
          <input
            type="text"
            value={friendLocation}
            onChange={(e) => setFriendLocation(e.target.value)}
            placeholder="Enter your friend’s address or city..."
            className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 outline-none"
          />
        </div>

        {/* Submit Button */}
        <button
          onClick={handleFindMidpoint}
          className="w-full py-3 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 active:scale-[0.98] transition-all duration-200"
        >
          Find the Midpoint
        </button>
      </div>
    </div>
  );
}
