# coding: utf-8
import logging
{% if cookiecutter.django_api != "🥷 django_ninja" %}
import json
{% endif %}
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

{% if cookiecutter.django_api == "🥷 django_ninja" %}
from ninja import Router

from .schemas import List{{cookiecutter.model}}Schema, {{cookiecutter.model_singular}}Schema, {{cookiecutter.model_singular}}SchemaIn
{% else %}
from django.views.decorators.http import require_http_methods

from ..commons.django_views_utils import ajax_login_required
{% endif %}

from .service import {{cookiecutter.model_lower}}_svc

{% if cookiecutter.django_api == "🥷 django_ninja" %}

router = Router()
{% endif %}
logger = logging.getLogger(__name__)


{% if cookiecutter.django_api == "🥷 django_ninja" %}
@router.post("/{{cookiecutter.model_lower}}/add", response={% raw %}{201{% endraw %}: {{cookiecutter.model_singular}}Schema{% raw %}}{% endraw %})
@csrf_exempt
def add_{{cookiecutter.model_singular_lower}}(request, {{cookiecutter.model_singular_lower}}: {{cookiecutter.model_singular}}SchemaIn):
    """Adiciona {{cookiecutter.model_singular}}"""
    logger.info("API add new {{cookiecutter.model_singular_lower}}.")
    new_{{cookiecutter.model_singular_lower}} = {{cookiecutter.model_lower}}_svc.add_{{cookiecutter.model_singular_lower}}({{cookiecutter.model_singular_lower}}.description)
{% else %}
@csrf_exempt
@ajax_login_required
def add_{{cookiecutter.model_singular_lower}}(request):
    """Adiciona {{cookiecutter.model_singular}}"""
    logger.info("API add new {{cookiecutter.model_singular_lower}}.")
    body = json.loads(request.body)
    description = body.get("description")

    if not description:
        raise ValueError("body.{{cookiecutter.model_singular_lower}}.description: Field required (missing)")
    if type(description) not in [str]:
        raise ValueError("body.{{cookiecutter.model_singular_lower}}.description: Input should be a valid string (string_type)")

    description = str(description)
    if len(description) <= 2:
        raise ValueError(
            "body.{{cookiecutter.model_singular_lower}}.description: Value error, It must be at least 3 characteres long. (value_error)"
        )

    new_{{cookiecutter.model_singular_lower}} = {{cookiecutter.model_lower}}_svc.add_{{cookiecutter.model_singular_lower}}(description)
{% endif %}
    return JsonResponse(new_{{cookiecutter.model_singular_lower}}, status=201)


{% if cookiecutter.django_api == "🥷 django_ninja" %}
@router.get("/{{cookiecutter.model_lower}}/list", response=List{{cookiecutter.model}}Schema)
{% else %}
@require_http_methods(["GET"])
@ajax_login_required
{% endif %}
def list_{{cookiecutter.model_lower}}(request):
    """Lista {{cookiecutter.model}}"""
    logger.info("API list {{cookiecutter.model_lower}}")
    {{cookiecutter.model_lower}} = {{cookiecutter.model_lower}}_svc.list_{{cookiecutter.model_lower}}()
    return JsonResponse({"{{cookiecutter.model_lower}}": {{cookiecutter.model_lower}}})
