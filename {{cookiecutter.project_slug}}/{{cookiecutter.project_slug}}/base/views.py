import os
from django.db import connection
from django.http import JsonResponse
{% if cookiecutter.django_api == "openapi" %}
from django.shortcuts import render
{% elif cookiecutter.django_api == "🥷 django_ninja" %}
from ninja import Router, Schema

router = Router()


class Error(Schema):
    message: str


@router.get("/dapau", response={500: Error}){% endif %}
def dapau(request):
    raise Exception("break on purpose")


{% if cookiecutter.django_api == "🥷 django_ninja" %}@router.get("/status"){% endif %}
def status(request):
    cursor = connection.cursor()
    cursor.execute("""SELECT 1+1""")
    row = cursor.fetchone()
    git_hash = os.getenv("GIT_HASH", "?")
    return JsonResponse(
        {
            "status": "ok",
            "db": "ok" if row == (2,) else "error",
            "git_hash": git_hash,
        }
    )


{% if cookiecutter.django_api == "📄 openapi" %}
def api_docs(request):
    return render(
        request,
        "base/apidocs.html",
        {"openapi_spec_url": "/api/openapi.json"},
    )
{% endif %}
