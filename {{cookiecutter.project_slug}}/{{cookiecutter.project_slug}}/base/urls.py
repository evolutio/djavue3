{% if cookiecutter.django_api == "django_ninja" %}
urlpatterns: list = []
{% elif cookiecutter.django_api == "openapi" %}
from django.urls import path

from . import views

urlpatterns = [
    path("", views.api_docs),
]
{% else %}
from django.urls import path

from . import views

urlpatterns = [
    path("dapau", views.dapau),
    path("status", views.status),
]
{% endif %}