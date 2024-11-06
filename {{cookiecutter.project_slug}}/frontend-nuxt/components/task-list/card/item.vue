<template>
    <v-list-item @click="task.done = !task.done">
        <template v-slot:prepend>
            <v-checkbox-btn v-model="task.done" color="grey"></v-checkbox-btn>
        </template>

        <v-list-item-title>
            <span :class="task.done
                ? 'text-grey text-decoration-line-through'
                : 'text-primary'
                ">{%raw%}{{ task.description }}{%endraw%}</span>
        </v-list-item-title>

        <template v-slot:append>
            <v-expand-x-transition>
                <v-icon v-if="task.done" color="success"> mdi-check </v-icon>
            </v-expand-x-transition>
        </template>
    </v-list-item>
</template>

<script setup lang="ts">
import type { Task } from '~/types/tasks';
const { task } = defineProps<{
    task: Task
}>()
</script>