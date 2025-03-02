<template>
  <nav>
    <router-link to="/">
      <div class="logo">sounds-like</div>
    </router-link>
    <ul class="menu">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/about">About</router-link></li>
      <li><router-link to="/contact">Contact</router-link></li>
    </ul>
  </nav>
</template>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background: #f3f1f5;
}

.logo {
  font-size: 1.5em;
  font-weight: bold;
  color: #623b83;
}

.menu {
  list-style: none;
  display: flex;
  gap: 20px;
}

.menu li a {
  text-decoration: none;
  color: #623b83;
  font-weight: 500;
  transition: color 0.3s;
}

.menu li a:hover {
  color: #623b83;
}

.menu li a.router-link-active {
  color: #9b31ad;
  font-weight: bold;
}
</style>
<script setup>
</script>