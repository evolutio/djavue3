# coding: utf-8
import logging
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
{% if cookiecutter.django_api == "🥷 django_ninja" %}
from ninja import Router

from .schemas import LoggedUserSchema, UserSchema, LoginSchema, Error
{% endif %}

logger = logging.getLogger(__name__)
{% if cookiecutter.django_api == "🥷 django_ninja" %}router = Router(){% endif %}

{% if cookiecutter.django_api == "🥷 django_ninja" %}
@router.post("/login", response={201: UserSchema, 401: Error})
@csrf_exempt
def login(request, data: LoginSchema):{% else %}
@csrf_exempt
def login(request):{% endif %}
    """
    Login do usuário e criação de uma nova sessão
    """
    logger.info("API login")
    username = {% if cookiecutter.django_api == "🥷 django_ninja" %}data.username{% else %}request.POST["username"]{% endif %}
    password = {% if cookiecutter.django_api == "🥷 django_ninja" %}data.password{% else %}request.POST["password"]{% endif %}
    user_authenticaded = auth.authenticate(username=username, password=password)
    user_dict = None
    if user_authenticaded is not None:
        if user_authenticaded.is_active:
            auth.login(request, user_authenticaded)
            user_dict = user_authenticaded.to_dict_json()
            logger.info("API login success")
    if not user_dict:
        user_dict = {"message": "Unauthorized"}
        return JsonResponse(user_dict, safe=False, status=401)
    return JsonResponse(user_dict, safe=False, status=201)


{% if cookiecutter.django_api == "🥷 django_ninja" %}@router.post("/logout"){% endif %}
def logout(request):
    """
    Encerra sessão do usuário
    """
    if request.method.lower() != "post":
        raise Exception("Logout only via post")
    logger.info(f"API logout: {request.user.username}")
    auth.logout(request)
    return JsonResponse({})


{% if cookiecutter.django_api == "🥷 django_ninja" -%}@router.get("/whoami", response=LoggedUserSchema){% endif %}
def whoami(request):
    """
    Retorna dados do usuário logado
    """
    user_data = {"authenticated": False}
    if request.user.is_authenticated:
        user_data["authenticated"] = True
        user_data["user"] = request.user.to_dict_json()

    logger.info("API whoami")
    return JsonResponse(user_data)
