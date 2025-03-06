import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import router from "./router";
import { OhVueIcon, addIcons } from "oh-vue-icons";
import {
  CoCheckCircle,
  BiXCircle,
  BiArrowRight,
  CoPlus,
  BiStack,
  BiShuffle,
  FcPrevious,
  IoPlay,
  FcNext,
  MdLoop,
  IoSearch,
  CoHome,
} from "oh-vue-icons/icons";

addIcons(
  CoCheckCircle,
  BiXCircle,
  BiArrowRight,
  CoPlus,
  BiStack,
  BiShuffle,
  FcPrevious,
  IoPlay,
  FcNext,
  MdLoop,
  IoSearch,
  CoHome
);

const app = createApp(App);
app.component("v-icon", OhVueIcon);
app.use(router);
app.mount("#app");
