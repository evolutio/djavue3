import type { AuthenticatedType, UserType } from "~/types/user";

export const useAccountStore = defineStore("account-store", () => {
  const loggedUser = ref<UserType | null | undefined>(undefined);
  const loading = ref(false);
  const { $api } = useNuxtApp();

  async function whoAmI() {
    try {
      const response: { user?: UserType; authenticated: boolean } = await $api(
        "/api/accounts/whoami"
      );
      const loggedIn = response.authenticated && response.user;
      loggedUser.value = null;
      if (loggedIn && response.user) {
        loggedUser.value = response.user;
      }
      return loggedUser.value;
    } catch (e) {
      console.log(e);
    }
    return null;
  }

  async function login(username: string, password: string) {
    loading.value = true;
    try {
      const response: UserType = await $api("api/accounts/login", {
        method: "post",
        body: { username, password },
      });
      loggedUser.value = response;
      navigateTo("/home");
      return response;
    } catch (e) {
      console.log(e);
    } finally {
      loading.value = false;
    }
    return null;
  }

  async function logout() {
    loading.value = true;
    try {
      const response: AuthenticatedType = await $api("api/accounts/logout", {
        method: "post",
      });
      if (!response.authenticated) {
        loggedUser.value = null;
      }
      navigateTo("/");
      return response;
    } catch (e) {
      console.log(e);
    } finally {
      loading.value = false;
    }
    return null;
  }

  return { login, logout, whoAmI, loading, loggedUser };
});
