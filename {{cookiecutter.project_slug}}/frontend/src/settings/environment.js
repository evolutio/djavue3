export const environment = {
  isDev: import.meta.env.MODE === "development",
  {%- if cookiecutter.api_mock == "mirageJS" -%}isMock: import.meta.env.VITE_API_MOCK === "true",{%- endif -%}
  apiBaseURL: import.meta.env.VITE_API_BASE_URL,
}
