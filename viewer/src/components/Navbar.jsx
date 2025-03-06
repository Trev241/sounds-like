import React from "react";
import { assets } from "../assets/assets";
const Navbar = () => {
  return (
    <>
      <div className="w-full flex justify-between items-center font-semibold">
        <div className="flex items-center gap-2">
          <img
            className="w-8 bg-[#121212] p-2 rounded-2xl cursor-pointer"
            src={assets.arrow_left}
            alt=""
          />
          <img
            className="w-8 bg-[#121212] p-2 rounded-2xl cursor-pointer"
            src={assets.arrow_right}
            alt=""
          />
        </div>
      </div>
      <div className="flex items-center gap-2 mt-4">
        <p className="bg-white  text-black px-4 py-1 rounded-2xl cursor-pointer">
          All
        </p>
        <p className="bg-white/10 text-white  px-4 py-1 rounded-2xl cursor-pointer">
          Rock{" "}
        </p>
        <p className="bg-white/10 text-white px-4 py-1 rounded-2xl cursor-pointer">
          Relax
        </p>
      </div>
    </>
  );
};

export default Navbar;
