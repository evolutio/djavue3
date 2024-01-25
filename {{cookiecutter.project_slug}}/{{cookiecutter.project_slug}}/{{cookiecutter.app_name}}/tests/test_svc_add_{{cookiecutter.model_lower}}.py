import pytest

from {{cookiecutter.project_slug}}.{{cookiecutter.app_name}}.models import {{cookiecutter.model_singular}}
from {{cookiecutter.project_slug}}.{{cookiecutter.app_name}}.service import {{cookiecutter.model_lower}}_svc
from {{cookiecutter.project_slug}}.base.exceptions import BusinessError


@pytest.mark.django_db
def test_deve_inserir_uma_nova_tarefa():
    new_item = {{cookiecutter.model_lower}}_svc.add_{{cookiecutter.model_singular_lower}}("ABC")

    item = {{cookiecutter.model_singular}}.objects.all().first()

    assert item.id == new_item.get("id")
    assert item.description == new_item.get("description")


@pytest.mark.django_db
def test_deve_retornar_um_erro_ao_cadastrar_item_sem_descricao():
    # Quando tentamos adicionar item sem valor
    with pytest.raises(BusinessError) as error:
        new_item = {{cookiecutter.model_lower}}_svc.add_{{cookiecutter.model_singular_lower}}(None)

    # Então
    assert str(error.value) == "Invalid description"


@pytest.mark.django_db
def test_deve_retornar_um_erro_ao_cadastrar_item_com_espacos_na_descricao():
    # Quando tentamos adicionar item sem valor
    with pytest.raises(BusinessError) as error:
        new_item = {{cookiecutter.model_lower}}_svc.add_{{cookiecutter.model_singular_lower}}("    ")

    # Então
    assert str(error.value) == "Invalid description"


@pytest.mark.django_db
def test_deve_aceitar_apenas_tipo_string_na_descricao():
    # Quando tentamos adicionar item sem valor
    with pytest.raises(BusinessError) as error:
        new_item = {{cookiecutter.model_lower}}_svc.add_{{cookiecutter.model_singular_lower}}(1000)

    # Então
    assert str(error.value) == "Invalid description"
