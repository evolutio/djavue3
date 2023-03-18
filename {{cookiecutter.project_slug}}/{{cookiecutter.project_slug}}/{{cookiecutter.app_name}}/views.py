# coding: utf-8
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import {{cookiecutter.model_lower}}_svc


@csrf_exempt
@ajax_login_required
def add_{{cookiecutter.model_singular_lower}}(request):
    {{cookiecutter.model_singular_lower}} = {{cookiecutter.model_lower}}_svc.add_{{cookiecutter.model_singular_lower}}(request.POST["description"])
    return JsonResponse({{cookiecutter.model_singular_lower}})


@ajax_login_required
def list_{{cookiecutter.model_lower}}(request):
    {{cookiecutter.model_lower}} = {{cookiecutter.model_lower}}_svc.list_{{cookiecutter.model_lower}}()
    return JsonResponse({"{{cookiecutter.model_lower}}": {{cookiecutter.model_lower}}})
