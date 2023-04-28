# coding: utf-8
{%- if cookiecutter.django_api == "django_ninja" -%}
from typing import List, Optional
{% else %}
import json
{%- endif -%}
from django.http import JsonResponse

{%- if cookiecutter.django_api == "django_ninja" -%}
from ninja import Router, Form, Schema
{% else %}
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
{%- endif -%}
from .service import {{cookiecutter.model_lower}}_svc

{%- if cookiecutter.django_api == "django_ninja" -%}
router = Router()


class TaskSchema(Schema):
    id: Optional[int]
    description: str
    done: bool = False


class ListTasksSchema(Schema):
    tasks: List[TaskSchema]
{%- endif -%}


{%- if cookiecutter.django_api == "django_ninja" -%}
@router.post("/tasks/add", response=TaskSchema)
def add_{{cookiecutter.model_singular_lower}}(request, task: TaskSchema):
    new_{{cookiecutter.model_singular_lower}} = {{cookiecutter.model_lower}}_svc.add_{{cookiecutter.model_singular_lower}}(task.description)
{% else %}
@csrf_exempt
@ajax_login_required
def add_{{cookiecutter.model_singular_lower}}(request):
    body = json.loads(request.body)
    new_{{cookiecutter.model_singular_lower}} = {{cookiecutter.model_lower}}_svc.add_{{cookiecutter.model_singular_lower}}(body.get("description"))
{%- endif -%}
    return JsonResponse(new_{{cookiecutter.model_singular_lower}})


{%- if cookiecutter.django_api == "django_ninja" -%}
@router.get("/tasks/list", response=ListTasksSchema)
{% else %}
@ajax_login_required
{%- endif -%}
def list_{{cookiecutter.model_lower}}(request{%- if cookiecutter.django_api == "django_ninja" %}, description: str = Form(...){% endif %}):
    {{cookiecutter.model_lower}} = {{cookiecutter.model_lower}}_svc.list_{{cookiecutter.model_lower}}()
    return JsonResponse({"{{cookiecutter.model_lower}}": {{cookiecutter.model_lower}}})
