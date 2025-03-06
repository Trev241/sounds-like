<script setup>
const props = defineProps(["image", "name", "desc"]);
</script>

<template>
  <div
    className="w-[200px] flex-shrink-0 text-center bg-gray-900 p-3 rounded-lg shadow-lg"
  >
    <img
      :src="props.image"
      :alt="props.name"
      className="w-full h-40 object-cover rounded-md"
    />
    <h2 className="text-white font-bold text-lg mt-2">{{ props.name }}</h2>
    <p className="text-gray-300 text-sm line-clamp">{{ props.desc }}</p>
  </div>
</template>
