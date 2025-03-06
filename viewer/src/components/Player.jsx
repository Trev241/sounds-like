import React, { useEffect, useRef } from "react";
import gsap from "gsap";
import { songsData } from "../assets/assets";
import { assets } from "../assets/assets";

const Player = () => {
  const controlsRef = useRef(null);
  const progressBarRef = useRef(null);
  const leftSectionRef = useRef(null);
  const rightSectionRef = useRef(null);

  useEffect(() => {
    const tl = gsap.timeline();

    tl.fromTo(
      controlsRef.current,
      { y: 30, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.6, ease: "power2.out" }
    )

      .fromTo(
        progressBarRef.current,
        { scaleX: 0, opacity: 0.6, transformOrigin: "center" },
        { scaleX: 1, opacity: 1, duration: 0.7, ease: "power2.out" },
        "-=0.3"
      )

      .fromTo(
        [leftSectionRef.current, rightSectionRef.current],
        { scale: 0.8, opacity: 0 },
        {
          scale: 1,
          opacity: 1,
          duration: 0.6,
          ease: "power2.out",
          stagger: 0.2,
        },
        "-=0.3"
      );
  }, []);

  return (
    <div className="w-full fixed bottom-0 left-0 h-[12%] backdrop-blur-lg flex items-center justify-between text-white px-6">
      {/* Left Section - Song Info */}
      <div ref={leftSectionRef} className="hidden lg:flex items-center gap-3">
        <img
          src={songsData[0].image}
          className="w-12 rounded-md shadow-lg"
          alt="Song"
        />
        <div>
          <p className="text-sm font-semibold">{songsData[0].name}</p>
          <p className="text-xs text-gray-400">
            {songsData[0].desc.slice(0, 12)}
          </p>
        </div>
      </div>

      {/* Center Section - Controls */}
      <div
        ref={controlsRef}
        className="flex flex-col items-center gap-2 flex-grow"
      >
        {/* Control Buttons */}
        <div className="flex gap-3">
          <img
            className="w-4 cursor-pointer opacity-80 hover:opacity-100"
            src={assets.shuffle_icon}
            alt="Shuffle"
          />
          <img
            className="w-4 cursor-pointer opacity-80 hover:opacity-100"
            src={assets.prev_icon}
            alt="Previous"
          />
          <img
            className="w-5 cursor-pointer opacity-100 hover:scale-105 transition-transform"
            src={assets.play_icon}
            alt="Play"
          />
          <img
            className="w-4 cursor-pointer opacity-80 hover:opacity-100"
            src={assets.next_icon}
            alt="Next"
          />
          <img
            className="w-4 cursor-pointer opacity-80 hover:opacity-100"
            src={assets.loop_icon}
            alt="Loop"
          />
        </div>

        {/* Progress Bar */}
        <div className="flex items-center gap-3 w-full max-w-[500px]">
          <p className="text-xs text-gray-400">1:06</p>
          <div
            ref={progressBarRef}
            className="relative w-full h-1 bg-gray-600 rounded-full cursor-pointer"
          >
            <div
              className="absolute h-1 bg-green-500 rounded-full"
              style={{ width: "0%" }}
            ></div>
          </div>
          <p className="text-xs text-gray-400">3:30</p>
        </div>
      </div>

      {/* Right Section - Extra Controls */}
      <div
        ref={rightSectionRef}
        className="hidden lg:flex items-center gap-2 opacity-80"
      >
        <img
          className="w-4 cursor-pointer hover:opacity-100"
          src={assets.plays_icon}
          alt="Plays"
        />
        <img
          className="w-4 cursor-pointer hover:opacity-100"
          src={assets.mic_icon}
          alt="Mic"
        />
        <img
          className="w-4 cursor-pointer hover:opacity-100"
          src={assets.queue_icon}
          alt="Queue"
        />
        <img
          className="w-4 cursor-pointer hover:opacity-100"
          src={assets.speaker_icon}
          alt="Speaker"
        />
        <img
          className="w-4 cursor-pointer hover:opacity-100"
          src={assets.volume_icon}
          alt="Volume"
        />

        {/* Volume Slider */}
        <div className="w-20 h-1 bg-gray-500 rounded-full cursor-pointer">
          <div
            className="h-1 bg-green-500 rounded-full"
            style={{ width: "0%" }}
          ></div>
        </div>

        <img
          className="w-4 cursor-pointer hover:opacity-100"
          src={assets.mini_player_icon}
          alt="Mini Player"
        />
        <img
          className="w-4 cursor-pointer hover:opacity-100"
          src={assets.zoom_icon}
          alt="Zoom"
        />
      </div>
    </div>
  );
};

export default Player;
