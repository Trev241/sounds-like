<script setup>
import { onMounted, ref } from "vue";
import gsap from "gsap";
import.meta.glob("/public/sounds/*.ogg");

const titleText = "Find that perfect song";
const title = ref(titleText.split(""));
let titleAnims = {};

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

  gsap.fromTo(
    "#about",
    {
      x: "100%",
    },
    { x: 0, duration: 2, ease: "power1.out", scrollTrigger: "#about" }
  );
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

    const filename = `key${noteIdx > 9 ? noteIdx : "0" + noteIdx}.ogg`;
    const audio = new Audio(`/sounds/${filename}`);
    audio.play();
  }

  let anim = titleAnims[id];
  if (!anim.isActive()) titleAnims[id].restart();
};

const onCharLeave = (event) => {
  // const id = event.target.id;
  // titleAnims[id].reverse();
};
</script>

<template>
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
        class="flex flex-col items-center justify-center text-center h-screen"
      >
        <h1 class="flex text-4xl font-extrabold tracking-[.3rem] mb-4">
          <div
            :id="'char-' + key"
            @mouseenter="onCharEnter"
            @mouseleave="onCharLeave"
            class="text-8xl title-char"
            v-for="(char, key) in title"
            :key="key"
          >
            <template v-if="char === ' '">&nbsp;</template>
            <template v-else>{{ char }}</template>
          </div>
        </h1>
        <p class="md:text-4xl">for whatever mood you're in</p>
      </div>

      <div class="flex justify-end items-center h-screen overflow-x-hidden">
        <div
          id="about"
          class="max-w-screen-xl font-tenor-sans flex-grow bg-white text-black p-8"
        >
          <h1 class="text-4xl font-extrabold mb-6">So what's all this?</h1>
          <p class="text-xl mb-4">
            sounds-like is the manifestation of a humble effort to learn how
            machine learning works. Whether your taste in music is mainstream or
            not, it is pretty pervasive in everyone's life. It's obviously
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
            has trained itself on the taste profile encompassing over 30k songs
            and 10k users. We would have loved to have trained on a much larger
            dataset but it's difficult when you're just a broke student.
          </p>
          <p class="text-xl">
            As for how this works, all you have to do is pick your top 4 from
            our dataset of songs. (No, we don't have that song that was released
            a month ago.) Our model will try to predict the probability chance
            of you interacting with each song in the dataset based on what you
            tell us. From this, we can deduce that items with the highest
            probability are songs that you are very likely to listen to. These
            are the songs we will recommend. It ain't much but it's honest work.
          </p>
        </div>
      </div>

      <div
        class="flex flex-col justify-evenly h-screen max-w-screen-xl mx-auto"
      >
        <div class="w-1/2 flex items-center">
          <div class="me-14 text-9xl">1.&nbsp;</div>
          <div>
            <h1 class="text-6xl font-extrabold mb-4">Pick your top four</h1>
            <p class="text-2xl">
              Let us know what you like best so that we can tell you the next
              best thing to listen to. Why just 4? No idea.
            </p>
          </div>
        </div>

        <div class="w-1/2 flex items-center">
          <div class="text-9xl">2.&nbsp;</div>
          <div>
            <h1 class="text-6xl font-extrabold mb-4">Check it out</h1>
            <p class="text-2xl">
              We'll judge your tastes to see if we can predict what you else you
              might like.
            </p>
          </div>
        </div>

        <div class="w-1/2 flex items-center">
          <div class="text-9xl">3.&nbsp;</div>
          <div>
            <h1 class="text-6xl font-extrabold mb-4">Learn why</h1>
            <p class="text-2xl">
              Visualize our reasoning for the prediction you received and make
              sense of it.
            </p>
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

#background-img {
  background-image: url("/images/bg-2.jpg");
  background-attachment: fixed;
  filter: brightness(25%);
}
</style>
