<template>
  <div>
    <v-card>
      <v-card-text>
        <v-text-field
          v-model="title"
          :label="formLabel"
          required
          outlined
          append-icon="fa-pen"
          @keyup.enter="addNew{{cookiecutter.model_singular}}" />
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    formLabel: {
      type: String,
      default: "",
    },
  },
  emits: ["new{{cookiecutter.model_singular}}"],
  data: () => {
    return {
      title: "",
    }
  },
  methods: {
    addNew{{cookiecutter.model_singular}}() {
      this.$emit("new{{cookiecutter.model_singular}}", {
        title: this.title,
      })
      this.title = ""
    },
  },
}
</script>

<style scoped></style>
