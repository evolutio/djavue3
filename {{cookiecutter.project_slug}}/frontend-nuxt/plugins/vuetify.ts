// import this after install `@mdi/font` package
import "@mdi/font/css/materialdesignicons.css";

import "vuetify/styles";
import { createVuetify } from "vuetify";
import { defineNuxtPlugin } from "nuxt/app";

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    theme: {
      defaultTheme: "light",
      themes: {
        light: {
          dark: false,
          colors: {
            primary: "#3451B2",
            secondary: "#5CBBF6",
          },
        },
      },
    },
  });
  app.vueApp.use(vuetify);
});
