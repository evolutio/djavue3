import pytest
from http import HTTPStatus


@pytest.mark.django_db
def test_deve_retornar_404_not_found_para_url_invalida(client, logged_jon):
    # Dado uma URL invalida
    payload = {"qualque": "coisa"}

    # Quando tentamos acessar
    resp = client.post(
        "/api/{{cookiecutter.app_name}}/{{cookiecutter.model_lower}}/invalid", payload, content_type="application/json"
    )

    # Entao 404
    assert resp.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.django_db
def test_deve_retornar_405_para_method_nao_existente(client, logged_jon):
    # Dado uma URL valida e metodo invalido
    payload = {"qualque": "coisa"}

    # Quando tentamos listar itens
    resp = client.post(
        "/api/{{cookiecutter.app_name}}/{{cookiecutter.model_lower}}/list", payload, content_type="application/json"
    )

    # Entao 405
    assert resp.status_code == HTTPStatus.METHOD_NOT_ALLOWED
