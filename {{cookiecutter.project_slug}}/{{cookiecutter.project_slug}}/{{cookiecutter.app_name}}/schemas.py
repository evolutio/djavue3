from typing import List

from ninja import Schema, ModelSchema
from pydantic import ConfigDict, field_validator
from .models import Task


class {{cookiecutter.model_singular}}SchemaIn(Schema):
    description: str

    @field_validator("description")
    def valid_description(cls, description: str) -> str:
        if description and len(description) <= 2:
            raise ValueError("It must be at least 3 characteres long.")
        return description


class {{cookiecutter.model_singular}}Schema(ModelSchema):
    class Meta:
        model = {{cookiecutter.model_singular}}
        fields = ["id", "description", "done"]

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 42,
                "description": "Task One",
                "done": True,
            }
        },
    )


class List{{cookiecutter.model}}Schema(Schema):
    {{cookiecutter.model_lower}}: List[{{cookiecutter.model_singular}}Schema]
