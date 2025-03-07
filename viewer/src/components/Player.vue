<script setup>
import gsap from "gsap";
import { ref, onMounted } from "vue";

const controlsRef = ref(null);
const progressRef = ref(null);
const leftSectRef = ref(null);

// Play/Pause State
const isPlaying = ref(false);

// Volume State
const volume = ref(50); // Default volume set to 50%

// Toggle Play/Pause
const togglePlay = () => {
  isPlaying.value = !isPlaying.value;
};

// GSAP Animations
onMounted(() => {
  const tl = gsap.timeline();

  tl.fromTo(
    controlsRef.value,
    { y: 30, opacity: 0 },
    { y: 0, opacity: 1, duration: 0.6, ease: "power2.out" }
  )
    .fromTo(
      progressRef.value,
      { scaleX: 0, opacity: 0.6, transformOrigin: "center" },
      { scaleX: 1, opacity: 1, duration: 0.7, ease: "power2.out" },
      "-=0.3"
    )
    .fromTo(
      leftSectRef.value,
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
});
</script>

<template>
  <div
    class="w-full fixed bottom-0 left-0 h-[10%] bg-[#181818] flex items-center justify-between text-white px-8 py-4 shadow-lg"
  >
    <!-- Left Section - Song Info -->
    <div ref="leftSectRef" class="hidden lg:flex items-center gap-4">
      <div>
        <p class="text-lg font-semibold">Song Name</p>
        <p class="text-sm text-gray-400">Artist Name</p>
      </div>
    </div>

    <!-- Center Section - Controls -->
    <div ref="controlsRef" class="flex flex-col items-center gap-3 flex-grow">
      <!-- Play/Pause Button -->
      <button
        @click="togglePlay"
        class="text-4xl text-white hover:scale-110 transition-transform duration-200"
      >
        <v-icon v-if="isPlaying" name="fa-pause" scale="2" />
        <v-icon v-else name="fa-play" scale="2" />
      </button>

      <!-- Progress Bar -->
      <div class="flex items-center gap-4 w-full max-w-[550px]">
        <p class="text-sm text-gray-400">1:06</p>
        <div
          ref="progressRef"
          class="relative w-full h-2 bg-gray-700 rounded-full cursor-pointer"
        >
          <div
            class="absolute h-2 bg-green-500 rounded-full"
            style="width: 30%"
          ></div>
        </div>
        <p class="text-sm text-gray-400">3:30</p>
      </div>
    </div>

    <!-- Right Section - Volume Control -->
    <div class="flex items-center gap-4">
      <v-icon
        name="bi-volume-down-fill"
        class="text-2xl text-white"
        scale="3"
      />
      <input
        type="range"
        min="0"
        max="100"
        v-model="volume"
        class="w-32 h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-green-500"
      />
      <p class="text-sm text-gray-400">{{ volume }}%</p>
    </div>
  </div>
</template>
