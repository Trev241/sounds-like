<script setup>
defineProps(["image", "name", "desc", "id"]);
</script>

<template>
  <div
    class="flex flex-col items-center min-w-[250px] w-full sm:w-1/2 md:w-1/3 lg:w-1/4 p-3 bg-gray-800 rounded-lg"
  >
    <img
      :src="image"
      alt="Song cover"
      class="w-full h-40 object-cover rounded-lg"
    />
    <h3 class="text-white text-lg font-semibold mt-2 text-center">
      {{ name }}
    </h3>
    <p class="text-gray-400 text-sm text-center">{{ desc }}</p>
  </div>
</template>
