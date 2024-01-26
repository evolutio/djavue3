import pytest

from {{cookiecutter.project_slug}}.{{cookiecutter.app_name}}.models import {{cookiecutter.model_singular}}
from {{cookiecutter.project_slug}}.{{cookiecutter.app_name}}.service import {{cookiecutter.model_lower}}_svc


@pytest.mark.django_db
def test_deve_retornar_lista_vazia():
    itens_list = {{cookiecutter.model_lower}}_svc.list_{{cookiecutter.model_lower}}()
    assert itens_list == []


@pytest.mark.django_db
def test_deve_listar_com_10_iten():
    # Dado 10 itens criados
    itens = [{{cookiecutter.model_singular}}(description=f"{{cookiecutter.model}} nro ${number}") for number in range(1, 11)]
    {{cookiecutter.model_singular}}.objects.bulk_create(itens)

    itens_list = {{cookiecutter.model_lower}}_svc.list_{{cookiecutter.model_lower}}()

    assert len(itens_list) == 10
