<script setup>
import { ref, computed, onMounted } from "vue";
import {
  fetchSongs,
  fetchRecommendedSongIds,
  fetchSongDetails,
} from "./api.js";
import vheader from "./Header.vue";
import sidebar from "./Sidebar.vue";
import player from "./Player.vue";

const likedSongs = ref([]);
const selectedSongs = ref([]);
const recommendedSongs = ref([]);
const activeSection = ref("available");
const trendingSongs = ref([]);

const likeSong = (song) => {
  if (likedSongs.value.some((s) => s.id === song.id)) {
    likedSongs.value = likedSongs.value.filter((s) => s.id !== song.id);
  } else {
    likedSongs.value.push(song);
  }
};

const loadsong = async () => {
  try {
    const songs = await fetchSongs();
    console.log(songs);
    trendingSongs.value = songs.map((song) => ({
      id: song.song_id,
      name: song.title,
      description: song.artist_name,
      image: song.image, // Ensure API provides images
    }));
  } catch (error) {
    console.error("Error fetching songs:", error);
  }
};

const selectSong = (song) => {
  if (selectedSongs.value.some((s) => s.id === song.id)) {
    selectedSongs.value = selectedSongs.value.filter((s) => s.id !== song.id);
  } else if (selectedSongs.value.length < 4) {
    selectedSongs.value.push(song);
  }

  if (selectedSongs.value.length === 4) {
    getRecommendations();
  }
};

const getRecommendations = async () => {
  activeSection.value = "recommended";

  const selectedSongIds = selectedSongs.value.map((s) => s.id);
  try {
    const recommendedSongIds = await fetchRecommendedSongIds(selectedSongIds);
    console.log(recommendedSongIds);

    if (!Array.isArray(recommendedSongIds) || recommendedSongIds.length === 0) {
      console.error(
        "Invalid recommended song IDs received:",
        recommendedSongIds
      );
      return;
    }

    const songDetailsPromises = recommendedSongIds.map((songId) =>
      fetchSongDetails(songId)
    );

    const songDetails = await Promise.all(songDetailsPromises);

    recommendedSongs.value = songDetails.filter((song) => song !== null);
  } catch (error) {
    console.error("Error fetching recommendations:", error);
  }
};

onMounted(() => {
  loadsong();
});
</script>

<template>
  <div class="h-screen bg-black flex flex-col font-sans overflow-auto">
    <vheader />

    <div class="flex flex-grow pt-[65px]">
      <div class="w-[320px] flex-shrink-0 bg-black">
        <sidebar />
      </div>

      <div class="flex-grow bg-black ml-2 px-6 pt-4 rounded">
        <h1 class="text-2xl font-bold mb-4 text-white">Song Recommendations</h1>

        <div class="flex justify-center gap-4 mb-4">
          <button
            @click="activeSection = 'available'"
            class="px-4 py-2 rounded-lg font-semibold transition"
            :class="
              activeSection === 'available'
                ? 'bg-blue-500 text-white'
                : 'bg-gray-700 text-gray-300'
            "
          >
            Available Songs
          </button>
          <button
            @click="activeSection = 'liked'"
            class="px-4 py-2 rounded-lg font-semibold transition"
            :class="
              activeSection === 'liked'
                ? 'bg-blue-500 text-white'
                : 'bg-gray-700 text-gray-300'
            "
          >
            Liked Songs
          </button>
          <button
            @click="activeSection = 'recommended'"
            class="px-4 py-2 rounded-lg font-semibold transition"
            :class="
              activeSection === 'recommended'
                ? 'bg-blue-500 text-white'
                : 'bg-gray-700 text-gray-300'
            "
          >
            Recommended Songs
          </button>
        </div>

        <div v-if="activeSection === 'available'" class="overflow-auto">
          <h2 class="text-xl font-semibold text-white mb-3">Available Songs</h2>
          <div
            v-for="song in trendingSongs"
            :key="song.id"
            class="flex items-center p-3 mb-2 bg-[#242424] rounded-lg"
          >
            <img
              :src="song.image"
              alt="Song Cover"
              class="w-12 h-12 rounded-md mr-4"
            />
            <div class="flex-grow">
              <h3 class="text-white font-medium">{{ song.name }}</h3>
              <p class="text-gray-400 text-sm">{{ song.description }}</p>
            </div>
            <button
              @click="likeSong(song)"
              class="ml-auto px-3 py-1 rounded-full transition font-bold"
              :class="
                likedSongs.some((s) => s.id === song.id)
                  ? 'bg-red-500 text-white'
                  : 'bg-white text-black'
              "
            >
              Like
            </button>
          </div>
        </div>

        <div v-if="activeSection === 'liked'" class="overflow-auto">
          <h2 class="text-xl font-semibold text-white mb-3">Liked Songs</h2>
          <div
            v-for="song in likedSongs"
            :key="song.id"
            class="flex items-center p-3 mb-2 bg-[#242424] rounded-lg"
          >
            <img
              :src="song.image"
              alt="Song Cover"
              class="w-12 h-12 rounded-md mr-4"
            />
            <h3 class="text-white font-medium">{{ song.name }}</h3>
            <button
              @click="selectSong(song)"
              class="ml-auto px-3 py-1 rounded-full transition font-bold"
              :class="
                selectedSongs.includes(song)
                  ? 'bg-green-500 text-white'
                  : 'bg-white text-black'
              "
            >
              Select
            </button>
          </div>
        </div>

        <div v-if="activeSection === 'recommended'" class="overflow-auto">
          <h2 class="text-xl font-semibold text-white mb-3">
            Recommended Songs
          </h2>
          <div
            v-for="song in recommendedSongs"
            :key="song.id"
            class="flex items-center p-3 mb-2 bg-[#242424] rounded-lg"
          >
            <div class="flex-grow">
              <h3 class="text-white font-medium">{{ song.title }}</h3>
              <p class="text-gray-400 text-sm">Artist: {{ song.artist }}</p>
              <p class="text-gray-400 text-sm">Release: {{ song.release }}</p>
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
