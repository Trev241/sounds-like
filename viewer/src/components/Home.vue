<script setup>
import { onMounted, ref } from "vue";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/all";

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
    y: -40,
    duration: 0.2,
    ease: "circ.out",
    color: "rgb(60, 60, 200)",
    stagger: {
      repeat: 1,
      yoyo: true,
      amount: 0.65,
    },
  });

  gsap
    .timeline({
      repeat: -1,
      paused: true,
      scrollTrigger: { trigger: "#pick-container", markers: true },
    })
    .fromTo(
      ".song",
      {
        filter: "grayscale(100%) blur(2px)",
        opacity: 0,
        x: "500%",
      },
      {
        opacity: 1,
        stagger: 0.1,
        x: 0,
        ease: "power4.out",
      }
    )
    .to(".chosen-song", {
      filter: "grayscale(0) blur(0)",
      stagger: 0.25,
    })
    .fromTo(
      ".verdict",
      {
        opacity: 0,
        y: 25,
      },
      { opacity: 1, stagger: 0.1, y: 0 },
      "+=1"
    )
    .add(() => {}, "+=5")
    .to(".verdict", { opacity: 0 })
    .to(".song", { x: "-500%", stagger: 0.1 }, "+=2")
    .add(() => {}, "+=2");

  gsap
    .timeline({
      repeat: -1,
      defaults: {
        ease: "power1.out",
      },
      scrollTrigger: {
        trigger: "#rec-container",
        start: "top bottom",
        markers: true,
      },
    })
    .set(".rec-text", { width: 0 })
    .fromTo(
      ".rec-song",
      { opacity: 0, y: -25 },
      {
        opacity: 1,
        y: 0,
        duration: 0.25,
        stagger: { amount: 5, repeat: 1, yoyo: true, repeatDelay: 3.25 },
      }
    )
    .to(
      ".rec-text",
      {
        width: "100%",
        duration: 1.75,
        stagger: { amount: 5, repeat: 1, yoyo: true },
      },
      "<"
    )
    .add(() => {}, "+=1");
});

const onCharEnter = (event) => {
  const id = event.target.id;
  const idInt = Number(id.split("-")[1]);
  const colorStep = Math.floor(255 / titleText.length);

  if (!(id in titleAnims))
    titleAnims[id] = gsap.to(`#${id}`, {
      // scale: 1.5,
      y: -40,
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
  <audio controls>
    <source src="http://127.0.0.1:8000/stream/SOBQJJX12A6D4F7F01" />
  </audio>

  <div class="relative min-h-screen">
    <div
      id="background-img"
      class="absolute inset-0 bg-cover bg-center bg-fixed"
    ></div>

    <div class="relative z-10 text-white">
      <!-- <div id="card-container" class="absolute inset-0">
        <div
          class="flex justify-evenly items-center bg-gray-900 h-screen font-extrabold"
        >
          <div
            id="card-1"
            class="w-full card flex items-center justify-center text-8xl h-full overflow-x-hidden"
          >
            Pop
          </div>
          <div
            id="card-2"
            class="w-full card flex items-center justify-center text-8xl h-full overflow-x-hidden"
          >
            Rock
          </div>
          <div
            id="card-3"
            class="w-full card flex items-center justify-center text-8xl h-full overflow-x-hidden"
          >
            EDM
          </div>
          <div
            id="card-4"
            class="w-full card flex items-center justify-center bg-gray-900 text-8xl h-full overflow-x-hidden"
          >
            Anything!
          </div>
        </div>
      </div> -->

      <div
        class="flex flex-col md:items-center md:text-center md:p-0 p-6 justify-center h-screen"
      >
        <div class="hidden md:contents">
          <h1 class="flex font-extrabold tracking-[.3rem] mb-4">
            <div
              :id="'char-' + key"
              @mouseenter="onCharEnter"
              class="text-8xl title-char"
              v-for="(char, key) in title"
              :key="key"
            >
              <template v-if="char === ' '">&nbsp;</template>
              <template v-else>{{ char }}</template>
            </div>
          </h1>
        </div>
        <h1 class="md:hidden text-6xl mb-4 font-extrabold">
          Find that perfect song
        </h1>
        <p class="text-xl md:text-4xl md:contents">
          for whatever mood you're in
        </p>
      </div>

      <!-- <div class="flex items-center h-screen overflow-x-hidden">
        <div
          id="about"
          class="font-tenor-sans flex-grow bg-white text-black p-8"
        >
          <div class="">
            <h1 class="text-4xl font-extrabold mb-6 text-center">
              So what's all this?
            </h1>
            <p class="text-xl mb-4">
              sounds-like is the manifestation of a humble effort to learn how
              machine learning works. Whether your taste in music is mainstream
              or not, it is pretty pervasive in everyone's life. It's obviously
              already been done before, perhaps even better, but why not try to
              predict what song someone might want to listen to?
            </p>
            <p class="text-xl mb-4">
              We are pretty good at telling friends the bangers apart from the
              trash but how do you make a machine do it? Imagine what a disaster
              it would be to be given <i>Thick of It</i> as a recommendation.
            </p>
            <p class="text-xl mb-4">
              Back to us, our model is designed on a simple neural network that
              has trained itself on the taste profile encompassing over 30k
              songs and 10k users. We would have loved to have trained on a much
              larger dataset but it's difficult when you're just a broke
              student.
            </p>
            <p class="text-xl">
              As for how this works, all you have to do is pick your top 4 from
              our dataset of songs. (No, we don't have that song that was
              released a month ago.) Our model will try to predict the
              probability chance of you interacting with each song in the
              dataset based on what you tell us. From this, we can deduce that
              items with the highest probability are songs that you are very
              likely to listen to. These are the songs we will recommend. It
              ain't much but it's honest work.
            </p>
          </div>
        </div>
      </div> -->

      <div
        class="flex flex-col min-h-screen max-w-screen-xl mx-auto md:py-24 md:p-0 p-6 overflow-x-hidden"
      >
        <div class="flex flex-col">
          <div class="md:w-1/2">
            <h1 class="text-5xl md:text-6xl font-commissioner mb-4">
              Pick your top 4
            </h1>
            <p class="text-xl md:text-2xl mb-8">
              Let us know what you like best so that we can tell you the next
              best thing to listen to. Why just 4? No idea.
            </p>
          </div>
          <div
            id="pick-container"
            class="flex flex-wrap md:flex-nowrap justify-evenly"
          >
            <div
              :id="key"
              class="w-1/2 md:w-1/5 flex flex-col items-center"
              v-for="(pick, key) in picks"
              :key="key"
            >
              <img :id="'song-' + key" :class="pick.class" :src="pick.src" />
              <v-icon class="verdict" :name="pick.icon" scale="5" />
            </div>
          </div>
        </div>
      </div>

      <div
        class="flex flex-col h-screen justify-center max-w-screen-xl mx-auto md:py-24 md:px-0 p-6"
      >
        <div class="flex items-center">
          <div class="md:w-1/2 mb-8">
            <h1 class="text-5xl md:text-6xl font-commissioner mb-4">
              Hear our verdict
            </h1>
            <p class="text-xl text-2xl">
              Get our recommendation based on what you told us. We can't
              guaranteee it will be perfect!
            </p>
          </div>
        </div>

        <div id="rec-container" class="flex flex-grow">
          <div class="relative w-full md:w-1/4">
            <div
              class="absolute inset-0"
              v-for="(verdict, key) in verdicts"
              :key="'img-' + key"
            >
              <img
                :id="'rec-song-' + key"
                :src="verdict.src"
                class="rounded-4xl rec-song"
              />
            </div>
          </div>

          <div class="relative flex-grow">
            <div
              class="absolute inset-0 rec-text"
              v-for="(verdict, key) in verdicts"
              :key="'text-' + key"
            >
              <div
                class="flex flex-col justify-center h-full mx-4 overflow-x-hidden"
              >
                <h1 class="text-6xl font-extrabold text-nowrap">
                  {{ verdict.title }}
                </h1>
                <p class="text-2xl text-nowrap">{{ verdict.artist }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div
        class="flex flex-col h-screen justify-center max-w-screen-xl mx-auto md:py-24 md:px-0 p-6"
      >
        <h1 class="text-5xl md:text-7xl font-extrabold mb-4">
          What are you waiting for?
        </h1>
        <h1 class="text-5xl md:text-7xl">
          Get started
          <router-link
            to="/qualify"
            class="underline cursor-pointer hover:text-pink-600"
            >here</router-link
          >
        </h1>
      </div>
    </div>
  </div>
</template>

<style>
.title-char {
  cursor: default;
}

#background-img {
  background-image: url("/images/bg-2.jpg");
  background-attachment: fixed;
  filter: brightness(25%);
}
</style>
