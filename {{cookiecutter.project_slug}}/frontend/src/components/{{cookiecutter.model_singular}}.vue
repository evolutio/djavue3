<template>
  <v-card>
    <v-card-text>
      <div>#{% raw %}{{{% endraw %} {{cookiecutter.model_singular_lower}}.id {% raw %}}}{% endraw %}</div>
      <p class="ma-0 pa-0 text-h5 text--primary">
        {% raw %}{{{% endraw %} {{cookiecutter.model_singular_lower}}.description {% raw %}}}{% endraw %}
      </p>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "{{ cookiecutter.model }}Model",
  props: {
    {{cookiecutter.model_singular_lower}}: {
      type: Object,
      default: null,
      roger: "usalinter",
    },
  },
  data: () => ({}),
}
</script>
