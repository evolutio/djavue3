import { Response } from "miragejs"
import Cookies from "js-cookie"

const getUserFromCookies = (schema) => {
  const userId = Cookies.get("sessionid")
  if (!userId) {
    return
  }
  return schema.users.find(userId)
}

export const {{cookiecutter.app_name}} = function (server) {
  server.config({
    routes() {
      this.namespace = "/api/{{cookiecutter.app_name}}/"

      this.get("/{{cookiecutter.model_lower}}/list", function (schema) {
        const loggedUser = getUserFromCookies(schema)
        if (!loggedUser) {
          return new Response(401, {}, "Header de segurança não encontrado")
        }
        return new Response(200, {}, schema.{{cookiecutter.model_lower}}.all())
      })

      this.post("/{{cookiecutter.model_lower}}/add", function (schema, request) {
        const attrs = JSON.parse(request.requestBody)
        const loggedUser = getUserFromCookies(schema)
        if (!loggedUser) {
          return new Response(401, {}, "Header de segurança não encontrado")
        }
        let new{{cookiecutter.model_singular}} = schema.{{cookiecutter.model_lower}}.create({
          description: attrs.description,
          userId: loggedUser.id,
        })
        return new Response(200, {}, new{{cookiecutter.model_singular}}.attrs)
      })
    },
  })
}
