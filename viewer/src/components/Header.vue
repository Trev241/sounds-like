<script setup>
import gsap from "gsap";
import { onMounted, ref } from "vue";

const placeholderText = ref("");
const header = ref(null);

onMounted(() => {
  // Animate header on mount
  gsap.fromTo(
    header.value,
    { y: -50, opacity: 0 },
    { y: 0, opacity: 1, duration: 1, ease: "power3.out" }
  );

  // Typing animation effect for the search bar placeholder
  const text = "What do you want to play?";
  let index = 0;

  const typePlaceholder = () => {
    if (index <= text.length) {
      placeholderText.value = text.substring(0, index);
      index++;
      setTimeout(typePlaceholder, 100);
    }
  };

  typePlaceholder();
});
</script>

<template>
  <div
    ref="header"
    class="fixed top-0 left-0 w-full h-[65px] z-50 bg-black flex items-center pr-28 pl-12 text-white text-lg shadow-lg"
  >
    <!-- Left Section: Icon, "Sound Like" Text, Search Bar -->
    <div class="flex items-center gap-5 flex-1 w-4/5">
      <v-icon name="bi-soundwave" scale="3" />
      <p
        class="font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600 text-xl"
      >
        Sound Like
      </p>
      <div
        class="flex items-center h-12 w-[420px] px-5 rounded-full border border-gray-600 bg-[#1e1e1e] focus-within:border-2 focus-within:border-white"
      >
        <v-icon name="io-search" />
        <input
          type="text"
          :placeholder="placeholderText"
          class="bg-transparent outline-none text-white w-full placeholder-gray-400 px-2 text-lg"
        />
      </div>
    </div>

    <!-- Right Section: About, Download, Login -->
    <div class="flex items-center gap-5 w-2/5 justify-end text-lg">
      <p class="cursor-pointer hover:opacity-80 font-medium">About</p>
      <p class="cursor-pointer hover:opacity-80 font-medium">Download</p>
      <span class="text-gray-500 text-xl">|</span>
      <button
        class="px-6 py-2 rounded-full bg-white text-black font-medium hover:bg-gray-200 text-lg"
      >
        Login
      </button>
    </div>
  </div>
</template>
