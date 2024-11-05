<template>
    <div style="height: 80dvh;" class="w-100 d-flex align-center justify-center">
        <LoginCard />
    </div>
</template>

<script setup lang="ts">
import type { MiddlewareKey } from '#build/types/middleware';
definePageMeta({
    middleware: 'unauthenticated' as MiddlewareKey
})
</script>