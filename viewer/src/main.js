import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import router from "./router";
import { OhVueIcon, addIcons } from "oh-vue-icons";
import { createPinia } from "pinia";
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
  BiSoundwave,
  FaPlay,
  FaPause,
  BiVolumeDownFill,
  BiBookmarkPlus,
  FcLike,
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
  CoHome,
  BiSoundwave,
  FaPlay,
  FaPause,
  BiVolumeDownFill,
  BiBookmarkPlus,
  FcLike
);

const app = createApp(App);
const pinia = createPinia();

app.component("v-icon", OhVueIcon);
app.use(pinia);
app.use(router);
app.mount("#app");
