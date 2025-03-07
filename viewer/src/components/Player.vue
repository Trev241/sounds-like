<script setup>
import gsap from "gsap";
import { ref, onMounted } from "vue";

const controlsRef = ref(null);
const progressRef = ref(null);
const leftSectRef = ref(null);

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
    className="w-full fixed bottom-0 left-0 h-[80px] sm:h-[12%] backdrop-blur-lg flex items-center justify-between text-white px-4 sm:px-6"
  >
    <!-- Left Section - Song Info -->
    <div ref="leftSectRef" className="hidden sm:flex items-center gap-3">
      <div>
        <p className="text-sm font-semibold">{songsData[0].name}</p>
        <p className="text-xs text-gray-400">
          {songsData[0].desc.slice(0, 12)}
        </p>
      </div>
    </div>

    <!-- Center Section - Controls -->
    <div
      ref="controlsRef"
      className="flex flex-col items-center gap-2 flex-grow"
    >
      <!-- Progress Bar -->
      <div className="flex items-center gap-3 w-full max-w-[500px]">
        <p className="text-xs text-gray-400 hidden sm:block">1:06</p>
        <div
          ref="progressRef"
          className="relative w-full h-1 bg-gray-600 rounded-full cursor-pointer"
        >
          <div
            className="absolute h-1 bg-green-500 rounded-full"
            style="width: 0"
          ></div>
        </div>
        <p className="text-xs text-gray-400 hidden sm:block">3:30</p>
      </div>
    </div>
  </div>
</template>