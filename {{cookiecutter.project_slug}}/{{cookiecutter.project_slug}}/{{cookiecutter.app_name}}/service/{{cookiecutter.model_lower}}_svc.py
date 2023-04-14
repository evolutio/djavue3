from ..models import {{cookiecutter.model_singular}}


def add_{{cookiecutter.model_singular_lower}}(new_{{cookiecutter.model_singular_lower}}):
    {{cookiecutter.model_singular_lower}} = {{cookiecutter.model_singular}}(description=new_{{cookiecutter.model_singular_lower}})
    {{cookiecutter.model_singular_lower}}.save()
    return {{cookiecutter.model_singular_lower}}.to_dict_json()


def list_{{cookiecutter.model_lower}}():
    {{cookiecutter.model_lower}} = {{cookiecutter.model_singular}}.objects.all()
    return [item.to_dict_json() for item in {{cookiecutter.model_lower}}]
