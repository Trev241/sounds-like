import React, { useEffect, useRef } from "react";
import gsap from "gsap";
import { assets } from "../assets/assets";

const Sidebar = () => {
  const sidebarRef = useRef(null);
  const createPlaylistRef = useRef(null);
  const getRecommendationsRef = useRef(null);

  useEffect(() => {
    // Timeline to control animations sequentially
    const tl = gsap.timeline();

    // Sidebar slide-in animation from the left
    tl.fromTo(
      sidebarRef.current,
      { x: -50, opacity: 0 },
      { x: 0, opacity: 1, duration: 1.5, ease: "power3.out" }
    )
      // Create Playlist animation - fades in from above after sidebar is loaded
      .fromTo(
        createPlaylistRef.current,
        { y: -20, opacity: 0 },
        { y: 0, opacity: 1, duration: 1, ease: "power3.out" },
        "+=0.3" // Delay after sidebar animation
      )
      // Get Recommendations animation - fades in from above the previous div
      .fromTo(
        getRecommendationsRef.current,
        { y: -20, opacity: 0 },
        { y: 0, opacity: 1, duration: 1, ease: "power3.out" },
        "-=0.5" // Starts slightly before the previous animation finishes for a smoother effect
      );
  }, []);

  return (
    <div
      ref={sidebarRef}
      className="bg-[#121212] h-[85%] w-[320px] rounded-xl mt-2 text-white"
    >
      <div className="p-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <img className="w-8" src={assets.stack_icon} alt="Library Icon" />
          <p className="font-semibold text-gray-300">Your Library</p>
        </div>
        <div className="flex items-center gap-3">
          <img src={assets.arrow_icon} className="w-5" alt="" />
          <img src={assets.plus_icon} className="w-5" alt="" />
        </div>
      </div>

      {/* Create Playlist Section */}
      <div
        ref={createPlaylistRef}
        className="p-4 bg-[#242424] m-2 rounded font-semibold flex flex-col items-start justify-start gap-1 pl-4"
      >
        <h1>Create your first playlist</h1>
        <p className="font-light">It's easy, we will help you</p>
        <button className="px-4 py-1.5 bg-white text-[15px] text-black rounded-full">
          Create Playlist
        </button>
      </div>

      {/* Get Recommendations Section */}
      <div
        ref={getRecommendationsRef}
        className="p-4 bg-[#242424] m-2 rounded font-semibold flex flex-col items-start justify-start gap-1 pl-4"
      >
        <h1>Get Personalized Recommendations</h1>
        <p className="font-light">Discover music tailored just for you</p>
        <button className="px-4 py-1.5 bg-white text-[15px] text-black rounded-full">
          Get Recommendations
        </button>
      </div>
    </div>
  );
};

export default Sidebar;
