import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import router from "./router";
import { OhVueIcon, addIcons } from "oh-vue-icons";
import { CoCheckCircle, BiXCircle } from "oh-vue-icons/icons";

addIcons(CoCheckCircle, BiXCircle);

const app = createApp(App);
app.component("v-icon", OhVueIcon);
app.use(router);
app.mount("#app");
