import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { createVuetify } from "vuetify";

const vuetify = createVuetify({});

createApp(App).use(router).use(store).use(vuetify).use(vuetify).mount("#app");
