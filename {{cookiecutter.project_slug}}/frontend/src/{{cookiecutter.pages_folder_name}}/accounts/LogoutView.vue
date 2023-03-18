<template>
  <v-container>
    <v-row align="start" no-gutters style="height: 150px">
      <v-col cols="12">
        <v-card class="text-center">
          <v-card-title class="headline"> Bye Bye </v-card-title>
          <v-card-text>
            <h2>Finalizar sessão?</h2>
            <p class="ma-4">
              <v-btn :loading="loading" color="primary" class="mr-4" x-large block @click="logout">
                SIM
              </v-btn>
              <v-btn
                class="my-2"
                block
                color="primary"
                variant="outlined"
                :to="{ name: 'base-home' }">
                Início
              </v-btn>
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useBaseStore } from "@/stores/baseStore"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  setup() {
    const baseStore = useBaseStore()
    const accountsStore = useAccountsStore()
    return { baseStore, accountsStore }
  },
  data: () => {
    return {
      loading: false,
    }
  },
  methods: {
    async logout() {
      this.loading = true
      const response = await this.accountsStore.logout()
      this.loading = false
      if (response) {
        this.baseStore.showSnackbar("Sessão encerrada!", "warning")
        this.$router.push({ name: "base-home" })
      }
    },
  },
}
</script>
