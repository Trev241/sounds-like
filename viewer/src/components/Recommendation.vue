<script setup>
import { ref, computed } from "vue";
import { songs } from "../data/songsData.js"; // Import songs data
import vheader from "./Header.vue";
import sidebar from "./Sidebar.vue";
import player from "./Player.vue";

const likedSongs = ref([]);
const selectedSongs = ref([]);
const recommendedSongs = ref([]);
const activeSection = ref("available"); // Controls which section is visible

// Function to Like a Song (Toggles Like)
const likeSong = (song) => {
  if (likedSongs.value.some((s) => s.id === song.id)) {
    likedSongs.value = likedSongs.value.filter((s) => s.id !== song.id);
  } else {
    likedSongs.value.push(song);
  }
};

// Function to Select a Song for Recommendation (Toggles Selection)
const selectSong = (song) => {
  if (selectedSongs.value.includes(song)) {
    selectedSongs.value = selectedSongs.value.filter((s) => s.id !== song.id);
  } else if (selectedSongs.value.length < 5) {
    selectedSongs.value.push(song);
  }

  // If five songs are selected, switch to "Recommended Songs" tab automatically
  if (selectedSongs.value.length === 5) {
    getRecommendations();
  }
};

// Function to Get Recommendations (Dummy Data)
const getRecommendations = () => {
  activeSection.value = "recommended";
  recommendedSongs.value = [
    {
      id: 6,
      name: "Recommended Song 1",
      description: "New vibes",
      image: "/images/rec1.jpg",
    },
    {
      id: 7,
      name: "Recommended Song 2",
      description: "Cool beats",
      image: "/images/rec2.jpg",
    },
    {
      id: 8,
      name: "Recommended Song 3",
      description: "Chill mood",
      image: "/images/rec3.jpg",
    },
  ];
};

// Circular Progress Meter (Calculated Percentage)
const progressPercentage = computed(
  () => (selectedSongs.value.length / 5) * 100
);
</script>

<template>
  <div class="h-screen bg-black flex flex-col font-sans overflow-auto">
    <!-- Header -->
    <vheader />

    <div class="flex flex-grow pt-[65px]">
      <!-- Sidebar -->
      <div class="w-[320px] flex-shrink-0 bg-black">
        <sidebar />
      </div>

      <!-- Main Content (Full Height Scrollable) -->
      <div class="flex-grow bg-black ml-2 px-6 pt-4 rounded">
        <h1 class="text-2xl font-bold mb-4 text-white">Song Recommendations</h1>

        <!-- Toggle Buttons -->
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

        <!-- Available Songs Section -->
        <div v-if="activeSection === 'available'" class="overflow-auto">
          <h2 class="text-xl font-semibold text-white mb-3">Available Songs</h2>
          <div
            v-for="song in songs"
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

        <!-- Liked Songs Section -->
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

          <!-- Circular Progress Bar -->
          <div class="flex flex-col items-center justify-center mt-6">
            <svg class="w-24 h-24">
              <circle
                class="text-gray-700"
                stroke-width="4"
                stroke="currentColor"
                fill="transparent"
                r="35"
                cx="50%"
                cy="50%"
              />
              <circle
                class="text-green-500 transition-all duration-500"
                stroke-width="4"
                :stroke-dasharray="220"
                :stroke-dashoffset="220 - progressPercentage * 2.2"
                stroke-linecap="round"
                stroke="currentColor"
                fill="transparent"
                r="35"
                cx="50%"
                cy="50%"
              />
            </svg>
            <p class="text-white mt-2">
              {{ selectedSongs.length }}/5 Songs Selected
            </p>
          </div>
        </div>

        <!-- Recommended Songs Section -->
        <div v-if="activeSection === 'recommended'" class="overflow-auto">
          <h2 class="text-xl font-semibold text-white mb-3">
            Recommended Songs
          </h2>
          <div
            v-for="song in recommendedSongs"
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
          </div>
        </div>
      </div>
    </div>

    <!-- Player (Fixed at Bottom) -->
    <div class="bg-black fixed bottom-0 w-full">
      <player />
    </div>
  </div>
</template>
