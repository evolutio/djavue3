<template>
    <div class="d-flex flex-column" style="max-width: 600px;">
        <h1 class="text-h4 text-md-h2 mb-2 text-primary font-weight-black">{%raw%}{{ title }}{%endraw%}</h1>
        <h1 class="description text-h4 text-md-h2 font-weight-black text-accent">
            {%raw%}{{ description }}{%endraw%}</h1>
        <p class="mt-4 text-h7 text-md-h5 text-grey-darken-1">{%raw%}{{ details }}{%endraw%}</p>
    </div>
</template>


<style scoped>
.description {
    opacity: 0.85;
}

@media (width>=960px) {
    .description {
        line-height: 4rem;
    }
}
</style>


<script setup lang="ts">
const { title, description, details } = defineProps<{
    title: string,
    description: string,
    details: string,
}>()
</script>
