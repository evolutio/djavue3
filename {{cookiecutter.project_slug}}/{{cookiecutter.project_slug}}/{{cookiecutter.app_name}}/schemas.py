from typing import List, Optional

from ninja import Schema


class TaskSchemaIn(Schema):
    description: str


class TaskSchema(Schema):
    id: Optional[int]
    description: str
    done: bool = False


class ListTasksSchema(Schema):
    tasks: List[TaskSchema]
