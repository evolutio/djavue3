import api from "./config.js"
import apiHelpers from "./helpers.js"

export default {
  whoami: async () => {
    const response = await api.get("/api/accounts/whoami")
    return response.data
  },
  login: async (username, password) => {
    const response = await api.post(
      "/api/accounts/login",
      apiHelpers.dataToForm({ username, password })
    )
    return response.data
  },
  logout: async () => {
    const response = await api.post("/api/accounts/logout")
    return response.data
  },
}
