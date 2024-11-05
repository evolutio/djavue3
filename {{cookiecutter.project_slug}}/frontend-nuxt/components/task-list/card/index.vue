<template>
    <v-card v-if="tasks.length > 0">
        <v-slide-y-transition class="py-0" tag="v-list" group>
            <template v-for="(task, i) in tasks" :key="`${i}-${task.description}`">
                <v-divider v-if="i !== 0" :key="`${i}-divider`"></v-divider>
                <TaskListCardItem :task="task" />
            </template>
        </v-slide-y-transition>
    </v-card>
</template>
<script setup lang="ts">
const taskStore = useTaskStore()
const { tasks: tasksRef } = storeToRefs(taskStore)
const tasks = computed(() => tasksRef.value)
</script>