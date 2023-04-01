from {{cookiecutter.project_slug}}.accounts.models import User


def user_jon():
    ze = User.objects.create_user(
        username="jon",
        first_name="Jon",
        last_name="Snow",
        email="jon@example.com",
        password="snow",
        bio="bio",
    )
    return ze
