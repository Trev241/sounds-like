import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Qualify from "../components/Qualify.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/qualify", component: Qualify },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
