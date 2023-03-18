<template>
  <v-snackbar
    v-model="showSnackbar"
    :color="snackbarCollors"
    multi-line
    location="center"
    elevation="12"
    content-class="snackbar-ft-size">
    {% raw %}{{ snackbarMessage }}{% endraw %}
  </v-snackbar>
</template>

<script>
import { mapState } from "pinia"
import { useBaseStore } from "@/stores/baseStore"

export default {
  setup() {
    const baseStore = useBaseStore()
    return { baseStore }
  },
  computed: {
    ...mapState(useBaseStore, ["snackbarMessage", "type", "showSnackbarMessage"]),
    showSnackbar: {
      get() {
        return this.showSnackbarMessage
      },
      set(value) {
        this.baseStore.showSnackbar(value)
      },
    },
    snackbarCollors() {
      const typeCollor = {
        success: "primary",
        danger: "red",
        warning: "orange",
      }
      return `${typeCollor[this.type || "success"]} accent-4`
    },
  },
}
</script>

<style>
.v-snackbar .snackbar-ft-size .v-snackbar__wrapper .v-snackbar__content {
  font-size: 1.1rem;
}
</style>
