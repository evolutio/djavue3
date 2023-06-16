# coding: utf-8
{% if cookiecutter.django_api != "django_ninja" %}
import json
{% endif %}
from django.http import JsonResponse

{% if cookiecutter.django_api == "django_ninja" %}
from ninja import Router

from .schemas import List{{cookiecutter.model}}Schema, {{cookiecutter.model_singular}}Schema, {{cookiecutter.model_singular}}SchemaIn
{% else %}
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
{% endif %}

from .service import {{cookiecutter.model_lower}}_svc

{% if cookiecutter.django_api == "django_ninja" %}

router = Router()
{% endif %}


{% if cookiecutter.django_api == "django_ninja" %}
@router.post("/{{cookiecutter.model_lower}}/add", response={{cookiecutter.model_singular}}Schema)
def add_{{cookiecutter.model_singular_lower}}(request, {{cookiecutter.model_singular_lower}}: {{cookiecutter.model_singular}}SchemaIn):
    new_{{cookiecutter.model_singular_lower}} = {{cookiecutter.model_lower}}_svc.add_{{cookiecutter.model_singular_lower}}({{cookiecutter.model_singular_lower}}.description)
{% else %}
@csrf_exempt
@ajax_login_required
def add_{{cookiecutter.model_singular_lower}}(request):
    body = json.loads(request.body)
    new_{{cookiecutter.model_singular_lower}} = {{cookiecutter.model_lower}}_svc.add_{{cookiecutter.model_singular_lower}}(body.get("description"))
{% endif %}
    return JsonResponse(new_{{cookiecutter.model_singular_lower}})


{% if cookiecutter.django_api == "django_ninja" %}
@router.get("/{{cookiecutter.model_lower}}/list", response=List{{cookiecutter.model}}Schema)
{% else %}
@ajax_login_required
{% endif %}
def list_{{cookiecutter.model_lower}}(request):
    {{cookiecutter.model_lower}} = {{cookiecutter.model_lower}}_svc.list_{{cookiecutter.model_lower}}()
    return JsonResponse({"{{cookiecutter.model_lower}}": {{cookiecutter.model_lower}}})
