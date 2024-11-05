<template>
    <v-row align="center" class="text-primary my-1">
        <strong class="mx-4 text-success-darken-2">
            Feitas: {%raw%}{{ completedTasks }}{%endraw%}
        </strong>

        <v-divider vertical></v-divider>

        <strong class="mx-4 text-info-darken-2">
            Restam: {%raw%}{{ remainingTasks }}{%endraw%}
        </strong>

        <v-divider vertical></v-divider>

        <strong class="mx-4 text-success-darken-2">
            Total: {%raw%}{{ tasks.length }}{%endraw%}
        </strong>

        <v-spacer></v-spacer>

        <v-progress-circular color="primary" v-model="progress" class="d-none d-md-flex me-2"></v-progress-circular>
    </v-row>
</template>
<script setup lang="ts">

const taskStore = useTaskStore()
const { tasks } = storeToRefs(taskStore)

const completedTasks = computed(() => {
    return tasks.value.filter((task) => task.done).length;
});

const progress = computed(() => {
    return (completedTasks.value / tasks.value.length) * 100;
});

const remainingTasks = computed(() => {
    return tasks.value.length - completedTasks.value;
});

</script>