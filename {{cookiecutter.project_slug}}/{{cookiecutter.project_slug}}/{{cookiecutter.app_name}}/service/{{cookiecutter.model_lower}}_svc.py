from ..models import {{cookiecutter.model_singular}}
from {{cookiecutter.project_slug}}.base.exceptions import BusinessError


def add_{{cookiecutter.model_singular_lower}}(new_{{cookiecutter.model_singular_lower}}: str) -> dict:
    if not isinstance(new_{{cookiecutter.model_singular_lower}}, str):
        raise BusinessError("Invalid description")

    if not new_{{cookiecutter.model_singular_lower}} or not new_{{cookiecutter.model_singular_lower}}.strip():
        raise BusinessError("Invalid description")

    {{cookiecutter.model_singular_lower}} = {{cookiecutter.model_singular}}(description=new_{{cookiecutter.model_singular_lower}})
    {{cookiecutter.model_singular_lower}}.save()
    return {{cookiecutter.model_singular_lower}}.to_dict_json()


def list_{{cookiecutter.model_lower}}():
    {{cookiecutter.model_lower}}_list = {{cookiecutter.model_singular}}.objects.all()
    return [item.to_dict_json() for item in {{cookiecutter.model_lower}}_list]
