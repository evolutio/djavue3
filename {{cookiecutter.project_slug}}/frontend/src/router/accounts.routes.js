// Composables
import EmptyLayout from "@/layouts/default/EmptyLayout.vue"
import LoginView from "@/{{cookiecutter.pages_folder_name}}/accounts/LoginView.vue"
import LogoutView from "@/{{cookiecutter.pages_folder_name}}/accounts/LogoutView.vue"

export default [
  {
    path: "/accounts",
    component: EmptyLayout,
    children: [
      {
        path: "login",
        name: "accounts-login",
        component: LoginView,
      },
      {
        path: "logout",
        name: "accounts-logout",
        component: LogoutView,
      },
    ],
  },
]
