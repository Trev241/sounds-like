import React, { useEffect, useRef } from "react";
import gsap from "gsap";
import Navbar from "./Navbar";
import { albumsData } from "../assets/assets";
import AlbumItem from "./AlbumItem";

const DisplayHome = () => {
  const albumContainerRef = useRef(null);

  useEffect(() => {
    const container = albumContainerRef.current;

    gsap.to(container, {
      x: "-50%", // Moves the album list to the left
      duration: 20, // Adjust speed (higher = slower)
      ease: "linear",
      repeat: -1, // Infinite loop
      modifiers: {
        x: (x) => `${parseFloat(x) % 50}%`, // Ensuring smooth loop
      },
    });
  }, []);

  return (
    <>
      <Navbar />
      <div className="my-5 font-bold text-2xl">
        <h1 className="my-5 text-bold text-2xl text-white">Featured Charts</h1>

        {/* Continuous Scrolling Effect */}
        <div className="w-full max-w-full overflow-hidden">
          <div
            className="flex gap-6 whitespace-nowrap"
            ref={albumContainerRef}
            style={{ width: "max-content" }} // Ensuring content doesn't shrink
          >
            {albumsData.concat(albumsData).map((item, index) => (
              <AlbumItem
                key={index}
                image={item.image}
                name={item.name}
                desc={item.desc}
                id={item.id}
              />
            ))}
          </div>
        </div>
      </div>
    </>
  );
};

export default DisplayHome;
