import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: null,
  }),
  actions: {
    setToken(token) {
      this.token = token;
      localStorage.setItem("authToken", token); // Persist across page reloads
    },
    loadToken() {
      this.token = localStorage.getItem("authToken");
    },
    clearToken() {
      this.token = null;
      localStorage.removeItem("authToken");
    },
  },
});
