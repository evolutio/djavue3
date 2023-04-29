{% if cookiecutter.django_api == "django_ninja" %}
urlpatterns = []
{% else %}
from django.urls import path

from . import views

urlpatterns = [
    path("dapau", views.dapau),
]
{% endif %}