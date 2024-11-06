import type { Task, TasksOutput } from "~/types/tasks";

export const useTaskStore = defineStore('task-store', () => {
    const tasks = ref<Task[]>([])
    const newTaskDescription = ref<string | null>(null)

    async function load() {
        const { $api } = useNuxtApp()
        try {
            const res = await $api<TasksOutput>("/api/core/tasks/list")
            tasks.value = res.tasks
        } catch (e) {
            console.log(e)
            tasks.value = []
        }
    }

    async function create() {
        if (newTaskDescription.value) {
            const { $api } = useNuxtApp();
            tasks.value.push({
                done: false,
                description: newTaskDescription.value,
                id: -1,
            });
            try {
                const newTask: Task = await $api("/api/core/tasks/add", {
                    method: "post",
                    body: {
                        description: newTaskDescription.value,
                    },
                });
                tasks.value[tasks.value.length - 1] = newTask
            } catch (e) {
                console.log(e);
                tasks.value.pop();
            }
    
            newTaskDescription.value = null;
        }
    }

    return { tasks, newTaskDescription, create, load }
})