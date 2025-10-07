import { NavLink } from "react-router-dom";

export default function Navbar() {
  const links = [
    { name: "Profile", path: "/" },
    { name: "Meet", path: "/meet" },
    { name: "Map", path: "/map" },
    { name: "Contact", path: "/contact" },
  ];

  return (
    <nav className="bg-white/80 backdrop-blur-md shadow-md fixed top-0 left-0 w-full z-50">
      <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
        {/* Logo */}
        <h1 className="text-2xl font-extrabold text-blue-600 tracking-tight hover:scale-105 transition-transform">
          SmartMeet
        </h1>

        {/* Navigation Links */}
        <ul className="flex space-x-8">
          {links.map((link) => (
            <li key={link.name}>
              <NavLink
                to={link.path}
                className={({ isActive }) =>
                  `text-gray-700 font-medium transition-colors duration-200 hover:text-blue-600 ${
                    isActive ? "text-blue-600 border-b-2 border-blue-600 pb-1" : ""
                  }`
                }
              >
                {link.name}
              </NavLink>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
}
