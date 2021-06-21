import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import MainLayout from "@/layouts/MainLayout.vue";

createApp(App)
  .use(router)
  .use(store)
  .component("MainLayout", MainLayout)
  .mount("#app");
