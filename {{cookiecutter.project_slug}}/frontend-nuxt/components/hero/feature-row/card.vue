<template>
    <v-card width="100%" variant="tonal" :title="title" :subtitle="subtitle" class="flex-fill pa-md-4" />
</template>

<script setup lang="ts">
defineProps<{
    title: string,
    subtitle: string,
}>()
</script>