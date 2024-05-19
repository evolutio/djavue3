import pytest
from unittest.mock import ANY

from {{cookiecutter.project_slug}}.accounts.models import User


def test_deve_retornar_usuario_nao_logado(client):
    resp = client.get("/api/accounts/whoami")

    assert resp.status_code == 200
    assert resp.json() == {"authenticated": False}


def test_deve_retornar_usuario_logado(client, logged_jon):
    resp = client.get("/api/accounts/whoami")

    data = resp.json()
    assert resp.status_code == 200
    assert data == {
        "user": {
            "id": ANY,
            "name": "Jon Snow",
            "username": "jon",
            "first_name": "Jon",
            "last_name": "Snow",
            "email": "jon@example.com",
            "avatar": None,
            "bio": "bio",
            "permissions": {"ADMIN": False, "STAFF": False},
        },
        "authenticated": True,
    }


@pytest.mark.django_db
def test_deve_fazer_login(client):
    jon = User.objects.create_user(
        username="jon",
        first_name="Jon",
        last_name="Snow",
        email="jon@example.com",
        password="snow",
        bio="bio",
    )

    resp = client.post(
        "/api/accounts/login",
        {"username": "jon", "password": "snow"},
        content_type="application/json",
    )
    login = resp.json()

    assert resp.status_code == 201
    assert login["email"] == "jon@example.com"

    resp = client.get("/api/accounts/whoami")
    data = resp.json()

    assert data == {
        "user": {
            "id": ANY,
            "name": "Jon Snow",
            "username": "jon",
            "first_name": "Jon",
            "last_name": "Snow",
            "email": "jon@example.com",
            "avatar": None,
            "bio": "bio",
            "permissions": {"ADMIN": False, "STAFF": False},
        },
        "authenticated": True,
    }


@pytest.mark.django_db
def test_deve_fazer_logout_quando_estiver_logado(client, logged_jon):
    resp = client.post("/api/accounts/logout")

    assert resp.status_code == 200
    assert not resp.json()


@pytest.mark.django_db
def test_deve_fazer_logout_mesmo_sem_login(client):
    resp = client.post("/api/accounts/logout")
    assert resp.status_code == 200
