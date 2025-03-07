<script setup>
import { onMounted, ref } from "vue";
import gsap from "gsap";

const sidebar = ref(null);
const playlist = ref(null);
const recommend = ref(null);

onMounted(() => {
  const tl = gsap.timeline();

  tl.fromTo(
    sidebar.value,
    { x: -50, opacity: 0 },
    { x: 0, opacity: 1, duration: 1.5, ease: "power3.out" }
  )
    .fromTo(
      playlist.value,
      { y: -20, opacity: 0 },
      { y: 0, opacity: 1, duration: 1, ease: "power3.out" },
      "+=0.3" 
    )
    .fromTo(
      recommend.value,
      { y: -20, opacity: 0 },
      { y: 0, opacity: 1, duration: 1, ease: "power3.out" },
      "-=0.5"
    );
});
</script>
<template>
  <div
    ref="sidebar"
    className="bg-[#121212] h-[85%] w-full sm:w-[320px] rounded-xl mt-2 text-white"
  >
    <div className="p-4 flex items-center justify-between">
      <div className="flex items-center gap-3">
        <v-icon name="bi-stack" class="w-6 h-6" />
        <p className="font-semibold text-gray-300 text-sm sm:text-base">Your Library</p>
      </div>
      <div className="flex items-center gap-3">
        <v-icon name="bi-arrow-right" class="w-5 h-5" />
        <v-icon name="co-plus" class="w-5 h-5" />
      </div>
    </div>

    
    <div
      ref="playlist"
      className="p-4 bg-[#242424] m-2 rounded font-semibold flex flex-col items-start justify-start gap-1 pl-4"
    >
      <h1 class="text-sm sm:text-base">Create your first playlist</h1>
      <p className="font-light text-xs sm:text-sm">It's easy, we will help you</p>
      <button
        className="px-4 py-1.5 bg-white text-[13px] sm:text-[15px] text-black rounded-full"
      >
        Create Playlist
      </button>
    </div>

  
    <div
      ref="recommend"
      className="p-4 bg-[#242424] m-2 rounded font-semibold flex flex-col items-start justify-start gap-1 pl-4"
    >
      <h1 class="text-sm sm:text-base">Get Personalized Recommendations</h1>
      <p className="font-light text-xs sm:text-sm">Discover music tailored just for you</p>
      <button
        className="px-4 py-1.5 bg-white text-[13px] sm:text-[15px] text-black rounded-full"
      >
        Get Recommendations
      </button>
    </div>
  </div>
</template>
