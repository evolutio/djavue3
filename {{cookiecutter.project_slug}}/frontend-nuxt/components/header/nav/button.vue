<template>
    <v-btn @click="navigate" variant="plain" class="text-primary font-weight-bold text-capitalize"
        style="text-decoration: none;">
        <slot></slot>
    </v-btn>
    <v-divider v-if="divider" class="py-auto" vertical inset thickness="2px" />
</template>

<script setup lang="ts">
const { href, divider } = defineProps<{
    href: string,
    divider?: boolean,
}>()
function navigate() {
    if (href.startsWith('http') && typeof window !== undefined) {
        window.location.replace(href)
    } else {
        navigateTo(href)
    }
}
</script>