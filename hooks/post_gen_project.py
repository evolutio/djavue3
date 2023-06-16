"""
    Remove unused code based on the cookiecutter answers
"""
import os
import random
import shutil

try:
    # Inspired by
    # https://github.com/django/django/blob/master/django/utils/crypto.py
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

DEBUG_VALUE = "debug"


def remove_github_actions_files():
    github_actions_dir = ".github"
    if os.path.exists(github_actions_dir):
        shutil.rmtree(github_actions_dir)


def remove_vscode_files():
    vscode_dirs = [".vscode"]
    for vscode_dir in vscode_dirs:
        if os.path.exists(vscode_dir):
            shutil.rmtree(vscode_dir)


def remove_vscode_devcontainer_files():
    vscode_dirs = [".devcontainer"]
    for vscode_dir in vscode_dirs:
        if os.path.exists(vscode_dir):
            shutil.rmtree(vscode_dir)


def fix_api_mock_mirageJS():
    shutil.rmtree("apimock")


def fix_api_mock_express():
    shutil.rmtree("frontend/src/apimock")


def remove_django_ninja_files(project_name, app_name):
    os.remove(f"{project_name}/{project_name}/api.py")
    os.remove(f"{project_name}/{app_name}/schemas.py")
    os.remove(f"{project_name}/accounts/schemas.py")


def remove_openapi_files(project_name):
    shutil.rmtree(f"{project_name}/base/templates/")
    os.remove(f"{project_name}/{project_name}/connexion.py")
    os.remove(f"{project_name}/{project_name}/openapi.yaml")


def remove_package_files():
    print(INFO + "  - 🗑️ Removing packaging api files" + TERMINATOR)
    REMOVE_PATHS = [
        '{% if cookiecutter.package_manager == "poetry" %} requirements.txt {% endif %}',
        '{% if cookiecutter.package_manager == "poetry" %} requirements-dev.txt {% endif %}',
        '{% if cookiecutter.package_manager != "poetry" %} pyproject.toml {% endif %}',
    ]

    for path in REMOVE_PATHS:
        path = path.strip()
        if path and os.path.exists(path):
            if os.path.isdir(path):
                os.rmdir(path)
            else:
                os.unlink(path)


def prepare_piptools(api_lib):
    os.rename("requirements.txt", "requirements.in")
    os.rename("requirements-dev.txt", "requirements-dev.in")
    os.rename(f"requirements-dev-txt-{api_lib}.pip", "requirements-dev.txt")

    if api_lib == "django_only":
        os.remove("requirements-dev-txt-django_ninja.pip")
        os.remove("requirements-dev-txt-openapi.pip")
    elif api_lib == "django_ninja":
        os.remove("requirements-dev-txt-django_only.pip")
        os.remove("requirements-dev-txt-openapi.pip")
    else:
        os.remove("requirements-dev-txt-django_only.pip")
        os.remove("requirements-dev-txt-django_ninja.pip")


def main():

    if "{{ cookiecutter.api_mock }}" == "mirageJS":
        print(INFO + "  - 🗑️ Removing Apimock express App files" + TERMINATOR)
        fix_api_mock_mirageJS()
    else:
        print(INFO + "  - 🗑️ Removing MirageJS files" + TERMINATOR)
        fix_api_mock_express()

    if "{{ cookiecutter.use_github_actions_CI }}".lower() != "yes":
        print(INFO + "  - 🗑️ Removing Github Actions workflow file" + TERMINATOR)
        remove_github_actions_files()

    if "{{ cookiecutter.keep_vscode_settings }}".lower() != "yes":
        print(INFO + "  - 🗑️ Removing VSCode files" + TERMINATOR)
        remove_vscode_files()

    if "{{ cookiecutter.keep_vscode_devcontainer }}".lower() != "yes":
        print(INFO + "  - 🗑️ Removing DevContainer files" + TERMINATOR)
        remove_vscode_devcontainer_files()

    if "{{ cookiecutter.django_api }}" != "django_ninja":
        print(INFO + "  - 🗑️ Removing django-ninja api files" + TERMINATOR)
        remove_django_ninja_files("{{ cookiecutter.project_slug }}", "{{ cookiecutter.app_name }}")
    else:
        print(INFO + "  Using django-ninja 🥷" + TERMINATOR)

    if "{{ cookiecutter.django_api }}" != "openapi":
        print(INFO + "  - 🗑️ Removing openapi API files" + TERMINATOR)
        remove_openapi_files("{{ cookiecutter.project_slug }}")
    else:
        print(INFO + "  Using openapi contract API" + TERMINATOR)

    remove_package_files()
    if "{{ cookiecutter.package_manager }}" == "pip-tools":
        print(INFO + "  Preparing piptools" + TERMINATOR)
        prepare_piptools("{{ cookiecutter.django_api }}")

    print(SUCCESS + "🐍 Your Django API backend is created! (root) ✨ 🍰 ✨\n\n" + HINT)
    print(
        SUCCESS + "🍰 Your Vue 3 frontend is created! (frontend folder) ✨ 🍰 ✨\n\n" + HINT
    )

    print("What's next?")
    print("  cd {{ cookiecutter.project_slug }}")
    print("  👉 For DOCKER users 🐳]")
    print("       docker compose build")
    print("       docker compose -d backend frontend")
    print("       go to http://localhost  (PORT is NOT necessary)")
    print("       docker compose exec -it backend bash")
    print("       ./manage.py createsuperuser")
    print("       pytest\n")

    print("  👉 For frontend devs 😎")
    print("       WIP\n")
    print("  👉 For backend devs 🦄]")
    print("       WIP\n")

    print(INFO + "⚠️ For more details, check the README\n" + TERMINATOR)


if __name__ == "__main__":
    main()
