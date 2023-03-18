<template>
  <v-footer :absolute="!fixed" app>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" lg="6" md="6" align-self="center" class="pa-0">
          <div class="px-5 text-grey text-center">
            <span v-if="user" class="pl-4">
              <v-icon>mdi-account</v-icon>
              {% raw %}{{ user.username }}{% endraw %}
            </span>
            <span class="px-5">ENV: {% raw %}{{ nodeEnv }}{% endraw %}</span>
          </div>
        </v-col>
        <v-col cols="12" lg="6" md="6" align-self="center" class="pa-0">
          <div class="px-5 text-grey text-center">
            <span class="px-5">API: {% raw %}{{ apiBaseUrl }}{% endraw %}</span>
          </div>
        </v-col>
        <v-col cols="12" align-self="center" class="pa-0 text-center">
          <span> &copy; {% raw %}{{ new Date().getFullYear() }}{% endraw %} - Djàvue Template </span>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  props: {
    fixed: {
      type: Boolean,
      default: true,
    },
    user: {
      type: Object,
      default: null,
    },
  },
  data: () => ({
    apiBaseUrl: import.meta.env.VITE_API_BASE_URL,
    nodeEnv: import.meta.env.VITE_NODE_ENV,
  }),
}
</script>
