from typing import List, Optional

from ninja import Schema


class {{cookiecutter.model_singular}}SchemaIn(Schema):
    description: str


class {{cookiecutter.model_singular}}Schema(Schema):
    id: Optional[int]
    description: str
    done: bool = False


class List{{cookiecutter.model}}Schema(Schema):
    {{cookiecutter.model_lower}}: List[{{cookiecutter.model_singular}}Schema]
