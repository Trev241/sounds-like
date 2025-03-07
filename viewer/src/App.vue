<script>
import NavBar from "./components/NavBar.vue";

export default {
  components: {
    NavBar,
  },
};
</script>

<template>
  <div class="font-poiret-one">
    <!-- <NavBar/> -->
    <router-view />
  </div>
</template>
