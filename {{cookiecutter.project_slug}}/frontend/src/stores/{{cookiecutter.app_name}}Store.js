import { defineStore } from "pinia"
import {{cookiecutter.app_name}}Api from "@/api/{{cookiecutter.app_name}}.api.js"

export const use{{cookiecutter.app_name}}Store = defineStore("{{cookiecutter.app_name}}Store", {
  state: () => ({
    {{cookiecutter.model_lower}}: [],
    {{cookiecutter.model_lower}}Loading: false,
  }),
  actions: {
    async get{{cookiecutter.model}}() {
      this.{{cookiecutter.model_lower}}Loading = true
      const response = await {{cookiecutter.app_name}}Api.get{{cookiecutter.model}}()
      this.{{cookiecutter.model_lower}} = response.{{cookiecutter.model_lower}}
      this.{{cookiecutter.model_lower}}Loading = false
    },
    async addNew{{cookiecutter.model_singular}}(tarefa) {
      const new{{cookiecutter.model_singular}} = await {{cookiecutter.app_name}}Api.addNew{{cookiecutter.model_singular}}(tarefa.title)
      return new{{cookiecutter.model_singular}}
    },
  },
})
