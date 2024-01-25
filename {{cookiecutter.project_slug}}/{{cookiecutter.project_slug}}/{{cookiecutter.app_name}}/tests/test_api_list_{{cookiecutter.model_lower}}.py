import pytest
from unittest.mock import ANY

from {{cookiecutter.project_slug}}.{{cookiecutter.app_name}}.models import {{cookiecutter.model_singular}}


def test_nao_deve_permitir_listar_{{cookiecutter.model_singular_lower}}_sem_login(client):
    # Dado um usuário anônimo

    # Quando tentamos listar itens
    resp = client.get("/api/{{cookiecutter.app_name}}/{{cookiecutter.model_lower}}/list")

    # Entao recebemos um sem autorizacao
    assert resp.status_code == 401


@pytest.mark.django_db
def test_deve_retornar_lista_vazia(client, logged_jon):
    # Quando tentamos listar itens
    resp = client.get("/api/{{cookiecutter.app_name}}/{{cookiecutter.model_lower}}/list")
    data = resp.json()

    # Entao recebemos um sem autorizacao
    assert resp.status_code == 200
    assert data.get("{{cookiecutter.model_lower}}") == []


@pytest.mark.django_db
def test_deve_listar_{{cookiecutter.model_singular_lower}}_com_login(client, logged_jon):
    # Dado um item criado
    {{cookiecutter.model_singular}}.objects.create(description="walk the dog")

    # Quando listamos
    resp = client.get("/api/{{cookiecutter.app_name}}/{{cookiecutter.model_lower}}/list")
    data = resp.json()

    # Entao
    assert resp.status_code == 200
    assert data == {
        "{{cookiecutter.model_lower}}": [{"description": "walk the dog", "done": False, "id": ANY}]
    }
