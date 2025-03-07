<script setup>
import { useAuthStore } from "../stores/auth";

const authStore = useAuthStore();

const hash = window.location.hash.substring(1);
const params = new URLSearchParams(hash);
const accessToken = params.get("access_token");
authStore.setToken(accessToken);
</script>

<template>
  <h1>All done</h1>
  <router-link to="/">Home</router-link>
</template>
