import vuetify, { transformAssetUrls } from "vite-plugin-vuetify"; // https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  app: {
    pageTransition: { name: 'page', mode: 'out-in' }
  },
  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  ssr: true,
  build: {
    transpile: ["vuetify"],
  },
  runtimeConfig: {
    public: {
      baseURL: process.env.NUXT_PUBLIC_BASE_URL,
    },
  },
  modules: [
    "@nuxtjs/google-fonts",
    "@vueuse/nuxt",
    "@nuxt/image",
    "@pinia/nuxt",
    (_options, nuxt) => {
      nuxt.hooks.hook("vite:extendConfig", (config) => {
        // @ts-expect-error
        config.plugins.push(vuetify({ autoImport: true }));
      });
    },
    //...
  ],
  image: {},
  googleFonts: {
    families: {
      Inter: [400, 700, 800],
    },
  },
  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },
});
