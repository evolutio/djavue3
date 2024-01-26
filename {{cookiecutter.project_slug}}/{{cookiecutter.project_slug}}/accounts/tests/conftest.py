import pytest

from {{cookiecutter.project_slug}}.accounts.models import User


@pytest.fixture
def user_jon(db):
    jon = User.objects.create_user(
        username="jon",
        first_name="Jon",
        last_name="Snow",
        email="jon@example.com",
        password="snow",
        bio="bio",
    )
    return jon


@pytest.fixture
def logged_jon(client, user_jon):
    client.force_login(User.objects.get(username=user_jon.username))
    return user_jon
