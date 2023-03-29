/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from "./App.vue"

// Composables
import { createApp } from "vue"

// Plugins
{% if cookiecutter.api_mock == "mirageJS" %}
import { mockServer } from "@/apimock"
{% endif %}
import { registerPlugins } from "@/plugins"

{% if cookiecutter.api_mock == "mirageJS" %}
// Settings
import { environment } from "@/settings"
{% endif %}

const app = createApp(App)

{% if cookiecutter.api_mock == "mirageJS" %}
if (environment.isDev && environment.isMock) {
  mockServer()
}
{% endif %}

registerPlugins(app)

app.mount("#app")
