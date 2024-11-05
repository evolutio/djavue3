<template>
    <v-container style="max-width: 500px;">
        <h1 class="text-h5 font-weight-bold text-center text-primary mb-4">
            Lista de tarefas
        </h1>
        <TaskListTextInput />
        <v-divider></v-divider>
        <TaskListOverview />
        <v-divider class="mb-4"></v-divider>
        <TaskListCard />
    </v-container>
</template>


<script setup lang="ts">
const taskStore = useTaskStore()
const { load } = taskStore;
onMounted(() => load())
</script>
