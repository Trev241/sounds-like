<template>
  <div class="home">
    <h1>sounds-like</h1>
    <p>Discover your next favorite song</p>
    <div class="cards">
      <div class="card">
        <h2>Start Now</h2>
        <p>aaa</p>
        <router-link to="/app" class="button">Go to App</router-link>
      </div>
      <div class="card">
        <h2>View Demo</h2>
        <p>aaa</p>
        <router-link to="/demo" class="button">View Demo</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  padding: 50px;
  color: #003087;
}

h1 {
  font-size: 3.5em;
  margin-bottom: 10px;
}

p {
  font-size: 1.3em;
  margin-bottom: 30px;
}

.cards {
  display: flex;
  justify-content: center;
  gap: 30px;
}

.card {
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  width: 400px;
  transition: transform 0.3s;
}

.card:hover {
  transform: scale(1.05);
}

.button {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #5b5ba1;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.button:hover {
  background-color: #191972;
}

@media (max-width: 768px) {
  .cards {
    flex-direction: column;
    align-items: center;
  }
}
</style>
<script setup>
</script>