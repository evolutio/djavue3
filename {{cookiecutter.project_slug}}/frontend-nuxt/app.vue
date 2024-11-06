<template>
  <NuxtLayout>
    <v-app>
      <div class="pa-4 pt-16 pa-md-16">
        <NuxtPage />
      </div>
    </v-app>
  </NuxtLayout>
</template>

<style>
@import url("~/assets/css/main.css");
.page-enter-active,
.page-leave-active {
  transition: all 0.4s;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
</style>