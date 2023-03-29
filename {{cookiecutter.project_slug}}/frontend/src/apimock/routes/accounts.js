import { Response } from "miragejs"
import Cookies from "js-cookie"

export const accounts = function (server) {
  server.config({
    routes() {
      this.namespace = "/api/accounts/"

      this.get("/whoami", function (schema) {
        const sessionId = Cookies.get("sessionid")

        if (!sessionId) {
          return new Response(200, {}, { authenticated: false })
        }

        const response = {
          user: schema.users.find(sessionId),
          authenticated: true,
        }

        return new Response(200, {}, response)
      })
      this.post("/login", function (schema, request) {
        const username = request.requestBody.get("username")
        const password = request.requestBody.get("password")
        const user = schema.users.findBy({ username: username, password: password })

        if (!user) {
          return new Response(200, {}, null)
        }

        Cookies.set("sessionid", `${user.id}`, { expires: 1 })
        return new Response(200, {}, user)
      })
      this.post("/logout", function () {
        Cookies.remove("sessionid")
        return new Response(
          200,
          {},
          {
            authenticated: false,
          }
        )
      })
    },
  })
}
