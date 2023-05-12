{% if cookiecutter.django_api != "django_only" %}
urlpatterns = []
{% else %}
from django.urls import path

from . import views

urlpatterns = [
    path("{{cookiecutter.model_lower}}/add", views.add_{{cookiecutter.model_singular_lower}}),
    path("{{cookiecutter.model_lower}}/list", views.list_{{cookiecutter.model_lower}}),
]
{% endif %}