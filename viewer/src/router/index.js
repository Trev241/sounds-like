import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Qualify from "../components/Qualify.vue";
import Recommendation from "../components/Recommendation.vue"; // Import the new Recommendation page
import Callback from "../components/Callback.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/qualify", component: Qualify },
  { path: "/recommendation", component: Recommendation }, // New route for recommendations
  { path: "/callback", component: Callback },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
