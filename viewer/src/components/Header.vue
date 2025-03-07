<script setup>
import gsap from "gsap";
import { onMounted, ref, useTemplateRef } from "vue";

let placeholderText = "";
const placeholderRef = ref(placeholderText);
const header = ref(null);

onMounted(() => {
  gsap.fromTo(
    header.value,
    { y: -50, opacity: 0 },
    { y: 0, opacity: 1, duration: 1, ease: "power3.out" }
  );

  const text = "What do you want to play?";
  let index = 0;
  const typePlaceholder = () => {
    if (index <= text.length) {
      placeholderText = text.substring(0, index);
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
    className="fixed top-0 left-0 w-full h-[65px] z-50 bg-black flex items-center px-4 sm:pr-28 sm:pl-12 text-white text-lg shadow-lg"
  >
    <!-- Left Section: Home Icon, "Sound Like" Text, Search Bar -->
    <div className="flex items-center gap-3 sm:gap-5 flex-1 w-4/5">
      <v-icon name="co-home" class="h-6 w-6" />
      <p
        className="font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600 text-xl hidden sm:block"
      >
        Sound Like
      </p>
      <div
        className="flex items-center h-10 sm:h-12 w-full sm:w-[420px] px-3 sm:px-5 rounded-full border border-gray-600 bg-[#1e1e1e] focus-within:border-2 focus-within:border-white"
      >
        <v-icon name="io-search" class="h-5 w-5 sm:h-6 sm:w-6" />
        <input
          type="text"
          :placeholder="placeholderRef"
          className="bg-transparent outline-none text-white w-full placeholder-gray-400 px-2 text-sm sm:text-lg"
        />
      </div>
    </div>

    <!-- Right Section: About, Download, Login -->
    <div className="hidden sm:flex items-center gap-5 w-2/5 justify-end text-lg">
      <p className="cursor-pointer hover:opacity-80 font-medium">About</p>
      <p className="cursor-pointer hover:opacity-80 font-medium">Download</p>
      <span className="text-gray-500 text-xl">|</span>
      <button
        className="px-6 py-2 rounded-full bg-white text-black font-medium hover:bg-gray-200 text-lg"
      >
        Login
      </button>
    </div>
  </div>
</template>
