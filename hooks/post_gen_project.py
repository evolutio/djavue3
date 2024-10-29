"""
    Remove unused code based on the cookiecutter answers
"""

import os
import random
import shutil

from pathlib import Path

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
FAIL = "\033[91m"
GREEN = "\x1b[1;32m "
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


def create_env_file():
    print(INFO + " - 💡 Creating .env File" + TERMINATOR)

    src_file = Path(".env.example")
    dst_file = Path(".env")

    shutil.copy(src_file, dst_file)

    print(INFO + " - ✅ Successfully Created .env File" + TERMINATOR)


def main():

    print("👉 {{ cookiecutter.package_manager }}")

    if (
        "{{ cookiecutter.deploy_to }}" == "fly.io"
        and "{{ cookiecutter.package_manager }}" not in ["requirements.txt", "poetry"]
    ):
        print(
            FAIL
            + "  🚀🚀🚀 ERRO: Opps, deploy com FLY.IO não funciona com package_manager: {{ cookiecutter.package_manager }}"
            + TERMINATOR
        )
        raise Exception("Opps!")

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

    if "{{ cookiecutter.django_api }}" != "🥷 django_ninja":
        print(INFO + "  - 🗑️ Removing django-ninja api files" + TERMINATOR)
        remove_django_ninja_files(
            "{{ cookiecutter.project_slug }}", "{{ cookiecutter.app_name }}"
        )
    else:
        print(INFO + "  Using django-ninja 🥷" + TERMINATOR)

    remove_package_files()

    create_env_file()

    print(SUCCESS + "🐍 Your Django API backend is created! (root) ✨ 🍰 ✨\n\n" + HINT)
    print(
        SUCCESS
        + "🍰 Your Vue 3 frontend is created! (frontend folder) ✨ 🍰 ✨\n\n"
        + HINT
    )

    print("What's next?")
    print("  cd {{ cookiecutter.project_slug }}")
    print("  👉 For DOCKER users 🐳")
    print("       docker compose build")
    print("       docker compose up")
    print("       go to http://localhost  (PORT is NOT necessary)")

    print("  👉 Using virtualenv 📦")
    print("       create a virtualenv")
    print("       install dependencies")

    print(GREEN + "\n  📄 for more information")
    print("       https://djavue3.vercel.app\n" + TERMINATOR)


if __name__ == "__main__":
    main()
