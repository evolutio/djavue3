<template>
    <ClientOnly>
        <v-switch key="dark-mode-switch" v-model="isDark" inset style="transform: scale(0.7)"
            true-icon="mdi-weather-night" false-icon="mdi-weather-sunny" hide-details />
        <template key="dark-mode-switch-loading" #fallback>
            <v-switch inset disabled loading style="transform: scale(0.7)" hide-details />
        </template>
    </ClientOnly>
    <HeaderNavDivider v-if="divider" />
</template>

<script setup lang="ts">
defineProps<{
    divider?: boolean
}>()
import { useTheme } from "vuetify";
import { useStorage } from "@vueuse/core";
const theme = useTheme();
const isDark = useStorage('is-dark', theme.global.current.value.dark)

function syncTheme() {
    theme.global.name.value = isDark.value ? 'dark' : 'light'
}

onMounted(syncTheme)

watch(isDark, syncTheme)

</script>