<template>
    <v-text-field v-model="newTaskDescription" @input="limitLength" label="Escreva uma tarefa aqui..." variant="solo"
        color="primary" @keydown.enter="create">
        <template v-slot:append-inner>
            <v-fade-transition>
                <v-btn color="primary" v-show="newTaskDescription" icon="mdi-plus-circle" variant="text"
                    @click="create"></v-btn>
            </v-fade-transition>
        </template>
    </v-text-field>
</template>

<script setup lang="ts">
const taskStore = useTaskStore()
const { create } = taskStore;
const { newTaskDescription } = storeToRefs(taskStore)

function limitLength() {
    if (newTaskDescription.value && newTaskDescription.value.length > 140) {
        newTaskDescription.value = newTaskDescription.value.slice(0, 140)
    }
}
</script>