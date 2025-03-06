import React from "react";
import { Route, Routes } from "react-router-dom";
import DisplayHome from "./DisplayHome";

const Display = () => {
  return (
    <div className="flex-grow  bg-black ml-2 px-6 pt-4 rounded overflow-auto">
      <Routes>
        <Route path="/" element={<DisplayHome />} />
      </Routes>
    </div>
  );
};

export default Display;
