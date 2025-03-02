<script>
import NavBar from './components/NavBar.vue';

export default {
  components: {
    NavBar,
  },
};
</script>

<template>
  <div class="wrapper">
    <NavBar/>
    <router-view/>
  </div>
</template>

<style>
.wrapper {
  background: #f3f1f5;
  min-height: 100vh;
  font-family: 'Roboto', sans-serif;
  position: relative;
  overflow: hidden;
}

.wrapper::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-repeat: repeat;
  animation: movePattern 30s linear infinite;
  z-index: -1;
}

@keyframes movePattern {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(100px, 100px);
  }
}
</style>