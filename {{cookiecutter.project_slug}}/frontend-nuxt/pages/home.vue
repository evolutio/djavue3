<template>
    <TaskList />
</template>

<script setup lang="ts">
import type { MiddlewareKey } from "#build/types/middleware";
definePageMeta({
    middleware: "authenticated" as MiddlewareKey,
});
</script>
