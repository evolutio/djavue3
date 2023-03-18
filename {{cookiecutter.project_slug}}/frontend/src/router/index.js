import { createRouter, createWebHistory } from "vue-router"
import accountsRoutes from "./accounts.routes"
import baseRoutes from "./base.routes"
import {{ cookiecutter.app_name }}Routes from "./{{ cookiecutter.app_name }}.routes"
import Page404View from "@/{{cookiecutter.pages_folder_name}}/base/Page404View.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    ...baseRoutes,
    ...accountsRoutes,
    ...{{ cookiecutter.app_name }}Routes,
    {
      path: "/:pathMatch(.*)*",
      name: "page-not-found-404",
      component: Page404View,
    },
  ],
})

export default router
