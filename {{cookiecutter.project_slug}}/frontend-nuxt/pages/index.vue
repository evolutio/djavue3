<template>
  <div class="d-flex mx-auto justify-center flex-column w-100" style="max-width: 1200px; margin-top: 80px;">
    <HeroMessage title="D-Jà Vue"
      description="Gerador de projeto full-stack, pronto para produção e focado na produtividade ⚡"
      details="Vue 3 | Vite | Vuetify e Backend Django 🦄 API" />
    <div>
      <v-btn @click="navigateTo('/login')" style="font-weight: 700;" variant="tonal" size="large"
        class="text-bold mt-8 text-capitalize bg-primary rounded-xl">Iniciar</v-btn>
    </div>
    <HeroFeatureRow />
  </div>
</template>

<script setup lang="ts">
import type { MiddlewareKey } from '#build/types/middleware';
definePageMeta({
  middleware: 'unauthenticated' as MiddlewareKey
})
useHead({
  title: 'D-jà Vue',
  meta: [
    { name: 'description', content: 'Gerador de projeto full-stack com Django e Vue' }
  ],
})
</script>
