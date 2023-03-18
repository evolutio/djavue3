import { defineStore } from "pinia"
import AccountsApi from "@/api/accounts.api.js"

export const useAccountsStore = defineStore("accountsStore", {
  state: () => ({
    loading: false,
    loggedUser: null,
  }),
  actions: {
    async whoAmI() {
      const response = await AccountsApi.whoami()
      const loggedIn = response.authenticated && response.user
      this.loggedUser = null
      if (loggedIn) {
        this.loggedUser = response.user
      }
      return this.loggedUser
    },
    async login(username, password) {
      this.loading = true
      const response = await AccountsApi.login(username, password)
      this.loading = false
      if (!response) {
        return
      }
      this.loggedUser = response
      return this.loggedUser
    },
    async logout() {
      this.loading = true
      const response = await AccountsApi.logout()
      this.loading = false
      if (!response.authenticated) {
        this.loggedUser = null
        return true
      }
      return false
    },
  },
})
