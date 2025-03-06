import React from "react";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import Player from "./components/Player";
import Display from "./components/Display";

const App = () => {
  return (
    <div className="h-screen bg-black flex flex-col">
      <Header />

      <div className="flex flex-grow pt-[65px]">
        <div className="w-[320px] flex-shrink-0">
          <Sidebar />
        </div>

        <div className="flex-grow overflow-hidden">
          <Display />
        </div>
      </div>

      <Player />
    </div>
  );
};

export default App;
