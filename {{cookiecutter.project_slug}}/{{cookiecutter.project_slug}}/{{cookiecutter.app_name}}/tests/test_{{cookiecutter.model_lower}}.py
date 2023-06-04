from unittest.mock import ANY

from {{cookiecutter.project_slug}}.accounts.models import User
from {{cookiecutter.project_slug}}.accounts.tests import fixtures
from {{cookiecutter.project_slug}}.{{ cookiecutter.app_name }}.models import {{cookiecutter.model_singular}}


def test_criar_{{cookiecutter.model_singular_lower}}_sem_login(client):
    resp = client.post("/api/{{cookiecutter.app_name}}/{{ cookiecutter.model_lower }}/add", {"new_{{cookiecutter.model_singular_lower}}": "walk the dog"})
    assert resp.status_code == 401


def test_criar_{{cookiecutter.model_singular_lower}}_com_login(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))
    payload = {"description": "estudar pytest"}
    resp = client.post("/api/{{cookiecutter.app_name}}/{{ cookiecutter.model_lower }}/add", payload, content_type="application/json")
    assert resp.status_code == 200


def test_listar_{{cookiecutter.model_singular_lower}}_com_login(client, db):
    fixtures.user_jon()
    {{cookiecutter.model_singular}}.objects.create(description="walk the dog")

    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/{{cookiecutter.app_name}}/{{ cookiecutter.model_lower }}/list")
    data = resp.json()

    assert resp.status_code == 200
    assert data == {
        "{{cookiecutter.model_lower}}": [{"description": "walk the dog", "done": False, "id": ANY}]
    }
