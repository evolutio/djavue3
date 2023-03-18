<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline"> {{ cookiecutter.model }} </v-card-title>
        </v-card>
      </v-col>

      <v-col cols="12">
        <{{cookiecutter.model_singular_lower}}-form :form-label="'New {{cookiecutter.model_singular}}'" @new-{{cookiecutter.model_singular_lower}}="addNew{{cookiecutter.model_singular}}" />
      </v-col>

      <v-col v-for="item in {{cookiecutter.model_lower}}" :key="item.id" cols="12">
        <{{cookiecutter.model_singular_lower}} :{{cookiecutter.model_singular_lower}}="item" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import { useBaseStore } from "@/stores/baseStore"
import { use{{ cookiecutter.app_name }}Store } from "@/stores/{{ cookiecutter.app_name }}Store"
import {{cookiecutter.model_singular}} from "@/components/{{cookiecutter.model_singular}}.vue"
import {{cookiecutter.model_singular}}Form from "@/components/{{cookiecutter.model_singular}}Form.vue"

export default {
  name: "{{ cookiecutter.model }}List",
  components: { {{cookiecutter.model_singular}}, {{cookiecutter.model_singular}}Form },
  setup() {
    const baseStore = useBaseStore()
    const {{ cookiecutter.app_name }}Store = use{{ cookiecutter.app_name }}Store()
    return { baseStore, {{ cookiecutter.app_name }}Store }
  },
  computed: {
    ...mapState(use{{ cookiecutter.app_name }}Store, ["{{cookiecutter.model_lower}}", "{{cookiecutter.model_lower}}Loading"]),
  },
  mounted() {
    this.get{{ cookiecutter.model }}()
  },
  methods: {
    get{{ cookiecutter.model }}() {
      this.{{ cookiecutter.app_name }}Store.get{{ cookiecutter.model }}()
    },
    async addNew{{cookiecutter.model_singular}}({{cookiecutter.model_singular_lower}}) {
      const new{{cookiecutter.model_singular}} = await this.{{cookiecutter.app_name}}Store.addNew{{cookiecutter.model_singular}}({{cookiecutter.model_singular_lower}})
      this.baseStore.showSnackbar(`New {{cookiecutter.model_singular_lower}} added #${ new{{cookiecutter.model_singular}}.id }`)
      this.get{{ cookiecutter.model }}()
    },
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
