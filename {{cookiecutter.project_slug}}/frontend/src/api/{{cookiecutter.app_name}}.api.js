import api from "./config.js"

export default {
  get{{ cookiecutter.model }}: async () => {
    const response = await api.get("/api/{{ cookiecutter.app_name }}/{{ cookiecutter.model_lower }}/list")
    return response.data
  },
  addNew{{cookiecutter.model_singular}}: async (description) => {
    const json = JSON.stringify({ description })
    const response = await api.post(
      "/api/{{ cookiecutter.app_name }}/{{ cookiecutter.model_lower }}/add",
      json
    )
    return response.data
  },
}
