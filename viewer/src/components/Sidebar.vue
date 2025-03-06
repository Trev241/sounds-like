<script setup>
import { onMounted, ref } from "vue";
import gsap from "gsap";

const sidebar = ref(null);
const playlist = ref(null);
const recommend = ref(null);

onMounted(() => {
  // Timeline to control animations sequentially
  const tl = gsap.timeline();

  // Sidebar slide-in animation from the left
  tl.fromTo(
    sidebar.value,
    { x: -50, opacity: 0 },
    { x: 0, opacity: 1, duration: 1.5, ease: "power3.out" }
  )
    // Create Playlist animation - fades in from above after sidebar is loaded
    .fromTo(
      playlist.value,
      { y: -20, opacity: 0 },
      { y: 0, opacity: 1, duration: 1, ease: "power3.out" },
      "+=0.3" // Delay after sidebar animation
    )
    // Get Recommendations animation - fades in from above the previous div
    .fromTo(
      recommend.value,
      { y: -20, opacity: 0 },
      { y: 0, opacity: 1, duration: 1, ease: "power3.out" },
      "-=0.5" // Starts slightly before the previous animation finishes for a smoother effect
    );
});
</script>
<template>
  <div
    ref="sidebar"
    className="bg-[#121212] h-[85%] w-[320px] rounded-xl mt-2 text-white"
  >
    <div className="p-4 flex items-center justify-between">
      <div className="flex items-center gap-3">
        <!-- <img className="w-8" src="{assets.stack_icon}" alt="Library Icon" /> -->
        <v-icon name="bi-stack" />
        <p className="font-semibold text-gray-300">Your Library</p>
      </div>
      <div className="flex items-center gap-3">
        <!-- <img src="{assets.arrow_icon}" className="w-5" alt="" />
        <img src="{assets.plus_icon}" className="w-5" alt="" /> -->
        <v-icon name="bi-arrow-right" />
        <v-icon name="co-plus" />
      </div>
    </div>

    <!-- Create Playlist Section -->
    <div
      ref="playlist"
      className="p-4 bg-[#242424] m-2 rounded font-semibold flex flex-col items-start justify-start gap-1 pl-4"
    >
      <h1>Create your first playlist</h1>
      <p className="font-light">It's easy, we will help you</p>
      <button
        className="px-4 py-1.5 bg-white text-[15px] text-black rounded-full"
      >
        Create Playlist
      </button>
    </div>

    <!-- Get Recommendations Section -->
    <div
      ref="recommend"
      className="p-4 bg-[#242424] m-2 rounded font-semibold flex flex-col items-start justify-start gap-1 pl-4"
    >
      <h1>Get Personalized Recommendations</h1>
      <p className="font-light">Discover music tailored just for you</p>
      <button
        className="px-4 py-1.5 bg-white text-[15px] text-black rounded-full"
      >
        Get Recommendations
      </button>
    </div>
  </div>
</template>
