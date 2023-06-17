"""mytodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
{% if cookiecutter.django_api == "openapi" %}
from pathlib import Path
{% endif %}
from django.contrib import admin
from django.urls import path{% if cookiecutter.django_api != "django_ninja" %}, include{% endif %}
from django.views.generic import TemplateView

{% if cookiecutter.django_api == "django_ninja" %}
from .api import api
{% elif cookiecutter.django_api == "openapi" %}
from .connexion import DjangoApi

APP_DIR = Path(__file__).parent.parent

apps_urls = DjangoApi(
    APP_DIR / "{{cookiecutter.project_slug}}" / "openapi.yaml", options={"swagger_url": "api"}
).urls
{% endif %}
urlpatterns = [
    path("admin/", admin.site.urls),
    {% if cookiecutter.django_api == "django_ninja" %}path("api/", api.urls),
    {% elif cookiecutter.django_api == "openapi" %}path("api/", apps_urls),
    path("api/docs", include("{{cookiecutter.project_slug}}.base.urls")),
    {% else %}path("api/", include("{{cookiecutter.project_slug}}.base.urls")),
    path("api/accounts/", include("{{cookiecutter.project_slug}}.accounts.urls")),
    path(
        "api/{{ cookiecutter.app_name }}/",
        include("{{cookiecutter.project_slug}}.{{ cookiecutter.app_name }}.urls"),
    ),{% endif %}
    path("", TemplateView.as_view(template_name="base/apihome.html")),
]
