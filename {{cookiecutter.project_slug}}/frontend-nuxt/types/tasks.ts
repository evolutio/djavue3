export type Task = {
    id: number;
    description: string;
    done: boolean;
};

export type TasksOutput = {
    tasks: Task[];
};