import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Profile from "./pages/Profile";
import Meet from "./pages/Meet";
import Map from "./pages/Map";
import Contact from "./pages/Contact";

export default function App() {
  return (
    <Router>
      <Navbar />
      <div className="max-w-6xl mx-auto mt-24 px-6">
        <Routes>
          <Route path="/" element={<Profile />} />
          <Route path="/meet" element={<Meet />} />
          <Route path="/map" element={<Map />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </Router>
  );
}
