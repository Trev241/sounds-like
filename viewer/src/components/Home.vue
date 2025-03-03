<script>
  console.log("test")
</script>

<template>
  <div class="relative min-h-screen">
    <div id="background-img" class="absolute inset-0 bg-cover bg-center bg-fixed"></div>

    <div class="relative z-10 text-white">
      <div class="flex flex-col items-center justify-center text-center h-screen">
        <h1 class="text-4xl md:text-8xl font-bold mb-4">Find that perfect song</h1>
        <p class="md:text-4xl">Or find something different</p>
      </div>

      <div class="flex flex-col items-center justify-center text-center h-screen">
        <h1 class="text-6xl">And learn how we decide what's right for you!</h1>
      </div>
    </div>
  </div>
</template>

<style>
  #background-img {
    background-image: url("/images/bg-2.jpg");
    background-attachment: fixed;
    filter: brightness(25%);
  }
</style>