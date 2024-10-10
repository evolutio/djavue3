{% if cookiecutter.django_api == "🥷 django_ninja" %}urlpatterns: list = []{% else %}
from django.urls import path

from . import views

urlpatterns = [
    path("dapau", views.dapau),
    path("status", views.status),
]
{% endif %}