{%- if cookiecutter.django_api != "🦄 django_only" -%}
urlpatterns: list = []
{% else %}
from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login),
    path('logout', views.logout),
    path('whoami', views.whoami),
]
{%- endif -%}
