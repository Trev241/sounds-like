import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import SuggestedMusic from "../components/SuggestedMusic.vue";
import Demo from "../components/Demo.vue";
import Contact from "../components/Contact.vue";
import About from "../components/About.vue";
import Qualify from "../components/Qualify.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/app", component: SuggestedMusic },
  { path: "/demo", component: Demo },
  { path: "/contact", component: Contact },
  { path: "/about", component: About },
  { path: "/qualify", component: Qualify },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
