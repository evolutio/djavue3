from typing import List, Optional

from ninja import Schema
from pydantic import validator


class {{cookiecutter.model_singular}}SchemaIn(Schema):
    description: str

    @validator("description")
    def valid_description(cls, description):
        if description and len(description) <= 2:
            raise ValueError("It must be at least 3 characteres long.")
        return description


class {{cookiecutter.model_singular}}Schema(Schema):
    id: Optional[int]
    description: str
    done: bool = False


class List{{cookiecutter.model}}Schema(Schema):
    {{cookiecutter.model_lower}}: List[{{cookiecutter.model_singular}}Schema]
