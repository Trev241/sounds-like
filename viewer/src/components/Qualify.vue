<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import vheader from "./Header.vue";
import sidebar from "./Sidebar.vue";
import player from "./Player.vue";
import Navbar from "./Navbar.vue";
import AlbumItem from "./AlbumItem.vue";
import SongItem from "./SongItem.vue";
import Recommendation from "./Recommendation.vue";
import { albumsData, songsData } from "../assets/assets.js";
import { fetchSongs } from "./api.js";

gsap.registerPlugin(ScrollTrigger);

const albumContainerRef = ref(null);
const songContainerRef = ref(null);
const showRecommendations = ref(false);
const trendingSongs = ref([]);

const loadSongs = async () => {
  const fetchedSongs = await fetchSongs();

  trendingSongs.value = fetchedSongs.map((song, index) => ({
    id: song.song_id,
    title: song.title,
    artist: song.artist_name,
    image: songsData[index % songsData.length].image,
  }));
};

onMounted(() => {
  loadSongs();

  if (albumContainerRef.value) {
    gsap.to(albumContainerRef.value, {
      x: "-50%",
      duration: 20,
      ease: "linear",
      repeat: -1,
      modifiers: {
        x: (x) => `${parseFloat(x) % 50}%`,
      },
    });
  }

  gsap.utils.toArray(".song-item").forEach((item) => {
    gsap.from(item, {
      opacity: 0,
      y: 50,
      duration: 1,
      ease: "power2.out",
      scrollTrigger: {
        trigger: item,
        start: "top 85%",
        toggleActions: "play none none none",
      },
    });
  });
});

onBeforeUnmount(() => {
  ScrollTrigger.getAll().forEach((t) => t.kill());
});
</script>

<template>
  <div class="h-screen bg-black flex flex-col font-sans">
    <vheader />

    <div class="flex flex-grow pt-[65px]">
      <div class="w-full sm:w-[320px] flex-shrink-0 bg-black">
        <sidebar @showRecommendations="showRecommendations = true" />
      </div>

      <div className="flex-grow overflow-hidden">
        <div
          className="flex-grow bg-black sm:ml-2 px-4 sm:px-6 pt-4 rounded overflow-auto"
        >
          <div class="flex-grow overflow-hidden">
            <div
              class="flex-grow bg-black ml-2 px-6 pt-4 rounded overflow-auto hide-scrollbar"
            >
              <Navbar />

              <div v-if="!showRecommendations">
                <div class="my-5 font-bold text-2xl">
                  <h1 class="my-5 text-bold text-2xl text-white">
                    Featured Charts
                  </h1>
                  <div class="w-full overflow-hidden">
                    <div
                      class="flex gap-6 whitespace-nowrap"
                      ref="albumContainerRef"
                      :style="{ width: 'max-content' }"
                    >
                      <AlbumItem
                        v-for="(item, index) in [...albumsData, ...albumsData]"
                        :key="index"
                        :image="item.image"
                        :name="item.name"
                        :desc="item.desc"
                        :id="item.id"
                      />
                    </div>
                  </div>
                </div>

                <!-- Trending Songs (Fetched from API) -->
                <div class="my-10 font-bold text-2xl">
                  <h1 class="my-5 text-bold text-2xl text-white">
                    Trending Songs
                  </h1>
                  <div class="w-full">
                    <div
                      class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-6 gap-y-8 w-full"
                      ref="songContainerRef"
                    >
                      <SongItem
                        v-for="(song, index) in trendingSongs"
                        :key="index"
                        :image="song.image"
                        :name="song.title"
                        :desc="song.artist"
                        :id="song.id"
                        class="song-item"
                      />
                    </div>
                  </div>
                </div>
              </div>

              <Recommendation v-if="showRecommendations" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-black fixed bottom-0 w-full">
      <player />
    </div>
  </div>
</template>
