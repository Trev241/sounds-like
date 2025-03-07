<script setup>
import vheader from "./Header.vue";
import sidebar from "./Sidebar.vue";
import player from "./Player.vue";
import gsap from "gsap";
import { onMounted } from "vue";

onMounted(() => {
  // const container = albumContainerRef;
  // gsap.to(container, {
  //   x: "-50%", // Moves the album list to the left
  //   duration: 20, // Adjust speed (higher = slower)
  //   ease: "linear",
  //   repeat: -1, // Infinite loop
  //   modifiers: {
  //     x: (x) => `${parseFloat(x) % 50}%`, // Ensuring smooth loop
  //   },
  // });
});
</script>
<template>
  <div className="h-screen bg-black flex flex-col">
    <vheader></vheader>

    <div className="flex flex-grow pt-[65px]">
      <div className="w-full sm:w-[320px] flex-shrink-0">
        <sidebar></sidebar>
      </div>

      <!-- Main Content Area -->
      <div className="flex-grow overflow-hidden">
        <div
          className="flex-grow bg-black sm:ml-2 px-4 sm:px-6 pt-4 rounded overflow-auto"
        >
          <!-- <div className="flex-grow overflow-hidden">
        <div
          className="flex-grow  bg-black ml-2 px-6 pt-4 rounded overflow-auto"
        >
          <Navbar />
          <div className="my-5 font-bold text-2xl">
            <h1 className="my-5 text-bold text-2xl text-white">
              Featured Charts
            </h1>

            <div className="w-full max-w-full overflow-hidden">
              <div
                className="flex gap-6 whitespace-nowrap"
                ref="{albumContainerRef}"
                :style="{ width: 'max-content' }"
              >
                {albumsData.concat(albumsData).map((item, index) => (
                <AlbumItem
                  key="{index}"
                  image="{item.image}"
                  name="{item.name}"
                  desc="{item.desc}"
                  id="{item.id}"
                />
                ))}
              </div>
            </div>
          </div>
        </div>
      </div> -->
        </div>
      </div>
    </div>

    <player></player>
  </div>
</template>
