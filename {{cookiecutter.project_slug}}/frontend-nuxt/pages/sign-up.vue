<template>
    <YouCanHelp />
</template>
<script setup lang="ts">
import type { MiddlewareKey } from '#build/types/middleware';
definePageMeta({
    middleware: 'unauthenticated' as MiddlewareKey
})
</script>