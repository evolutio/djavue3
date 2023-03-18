"""
WSGI config for {{cookiecutter.project_slug}} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}.settings",
)

application = get_wsgi_application()
