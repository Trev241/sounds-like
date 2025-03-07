<script setup>
import { onMounted, ref } from "vue";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/all";
import.meta.glob("/public/sounds/*.ogg");

gsap.registerPlugin(ScrollTrigger);

const titleText = "Find that perfect song";
const title = ref(titleText.split(""));
let titleAnims = {};

const songs = [
  "/images/cropped-song-1.jpg",
  "/images/cropped-song-2.jpg",
  "/images/cropped-song-3.jpg",
  "/images/cropped-song-4.jpg",
  "/images/cropped-song-5.jpg",
];
const badPick = Math.floor(Math.random() * songs.length);
const picks = ref(
  songs.map((song, idx) => ({
    src: song,
    chosen: idx === badPick ? false : true,
    icon: idx === badPick ? "bi-x-circle" : "co-check-circle",
    class: `rounded-4xl ${idx === badPick ? "" : "chosen-song"} song p-2`,
  }))
);

const verdicts = ref([
  { src: "/images/cropped-rec-song-1.jpg", title: "MONEY", artist: "Lisa" },
  {
    src: "/images/cropped-rec-song-2.jpg",
    title: "Renai Circulation",
    artist: "Kana Hanazawa",
  },
]);

onMounted(() => {
  gsap.to(".title-char", {
    y: -20,
    duration: 0.2,
    ease: "circ.out",
    color: "rgb(60, 60, 200)",
    stagger: {
      repeat: 1,
      yoyo: true,
      amount: 0.65,
    },
  });

  let songTimeline = gsap.timeline({
    repeat: -1,
    paused: true,
    scrollTrigger: { trigger: "#pick-container", markers: true },
  });
  songTimeline.fromTo(
    ".song",
    {
      filter: "grayscale(100%) blur(2px)",
      opacity: 0,
      x: "100%",
    },
    {
      opacity: 1,
      stagger: 0.1,
      x: 0,
      ease: "power4.out",
    }
  );
  songTimeline.to(".chosen-song", {
    filter: "grayscale(0) blur(0)",
    stagger: 0.25,
  });
  songTimeline.fromTo(
    ".verdict",
    {
      opacity: 0,
      y: 25,
    },
    { opacity: 1, stagger: 0.1, y: 0 },
    "+=1"
  );
  songTimeline.add(() => {}, "+=5");
  songTimeline.to(".verdict", { opacity: 0 });
  songTimeline.to(".song", { x: "-100%", stagger: 0.1 }, "+=2");
  songTimeline.add(() => {}, "+=2");

  let recTimeline = gsap.timeline({
    repeat: -1,
    ease: "power4.out",
    scrollTrigger: {
      trigger: "#rec-container",
      start: "top bottom",
      markers: true,
    },
  });
  recTimeline.set(".rec-text", { width: 0 });
  recTimeline.to(".rec-text", {
    width: "100%",
    duration: 2,
    stagger: { amount: 6, repeat: 1, yoyo: true },
  });
  recTimeline.add(() => {}, "+=3");
});

const onCharEnter = (event) => {
  const id = event.target.id;
  const idInt = Number(id.split("-")[1]);
  const colorStep = Math.floor(255 / titleText.length);

  if (!(id in titleAnims))
    titleAnims[id] = gsap.to(`#${id}`, {
      y: -20,
      duration: 0.4,
      ease: "power4.out",
      color: `rgb(${idInt * colorStep}, ${255 - idInt * colorStep}, 200)`,
      repeat: 1,
      yoyo: true,
    });

  if (titleText[idInt] !== " ") {
    let noteIdx = idInt + 1;
    if (noteIdx > 4) noteIdx--;
    if (noteIdx > 9) noteIdx--;
    if (noteIdx > 16) noteIdx--;

    const filename = `key${noteIdx > 9 ? noteIdx : "0" + noteIdx}.mp3`;
    const audio = new Audio(`/sounds/${filename}`);
    audio.play();
  }

  let anim = titleAnims[id];
  if (!anim.isActive()) titleAnims[id].restart();
};
</script>

<template>
  <div class="relative min-h-screen">
    <div
      id="background-img"
      class="absolute inset-0 bg-cover bg-center bg-fixed"
      style="background-image: url('/images/bg-2.jpg'); filter: brightness(25%);"
    ></div>

    <div class="relative z-10 text-white">
      <div class="flex flex-col items-center justify-center text-center h-screen">
        <h1 class="flex flex-wrap justify-center text-4xl sm:text-6xl md:text-8xl font-extrabold tracking-[.3rem] mb-4">
          <div
            :id="'char-' + key"
            @mouseenter="onCharEnter"
            class="text-4xl sm:text-6xl md:text-8xl title-char"
            v-for="(char, key) in title"
            :key="key"
          >
            <template v-if="char === ' '">&nbsp;</template>
            <template v-else>{{ char }}</template>
          </div>
        </h1>
        <p class="text-xl sm:text-2xl md:text-4xl">for whatever mood you're in</p>
      </div>

      <div class="flex flex-col min-h-screen max-w-screen-xl mx-auto py-12 sm:py-24 overflow-x-hidden">
        <div class="w-full px-4 sm:px-0">
          <h1 class="text-4xl sm:text-6xl font-commissioner mb-4">Pick your top 4</h1>
          <p class="text-lg sm:text-2xl mb-8">
            Let us know what you like best so that we can tell you the next best thing to listen to. Why just 4? No idea.
          </p>
        </div>
        <div id="pick-container" class="flex flex-col sm:flex-row justify-evenly gap-4 sm:gap-0">
          <div
            :id="key"
            class="w-full sm:w-1/5 flex flex-col items-center"
            v-for="(pick, key) in picks"
            :key="key"
          >
            <img :id="'song-' + key" :class="pick.class" :src="pick.src" class="w-full sm:w-auto" />
            <v-icon class="verdict" :name="pick.icon" scale="2 sm:scale-3 md:scale-4 lg:scale-5" />
          </div>
        </div>
      </div>

      <div class="flex flex-col h-screen justify-center max-w-screen-xl mx-auto py-12 sm:py-24">
        <div class="flex flex-col sm:flex-row items-center px-4 sm:px-0">
          <div class="w-full sm:w-1/2 mb-8">
            <h1 class="text-4xl sm:text-6xl font-commissioner mb-4">Hear our verdict</h1>
            <p class="text-lg sm:text-2xl">
              Get our recommendation based on what you told us. We can't guarantee it will be perfect!
            </p>
          </div>
        </div>

        <div id="rec-container" class="flex flex-col sm:flex-row flex-grow px-4 sm:px-0">
          <div class="relative w-full sm:w-1/4 mb-8 sm:mb-0">
            <div
              class="absolute inset-0"
              v-for="(verdict, key) in verdicts"
              :key="'img-' + key"
            >
              <img :src="verdict.src" class="rounded-4xl rec-song w-full sm:w-auto" />
            </div>
          </div>

          <div class="relative w-full sm:flex-grow">
            <div
              class="absolute inset-0 rec-text"
              v-for="(verdict, key) in verdicts"
              :key="'text-' + key"
            >
              <div
                class="flex flex-col justify-center h-full m-4 overflow-x-hidden"
              >
                <h1 class="text-4xl sm:text-6xl font-extrabold text-nowrap">
                  {{ verdict.title }}
                </h1>
                <p class="text-lg sm:text-2xl text-nowrap">{{ verdict.artist }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.title-char {
  cursor: default;
}
</style>