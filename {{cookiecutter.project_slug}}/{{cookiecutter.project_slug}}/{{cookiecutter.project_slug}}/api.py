from ninja import NinjaAPI
from ninja.security import django_auth
from ninja.errors import ValidationError
from django.http import JsonResponse

from ..base.views import router as base_router
from ..accounts.views import router as accounts_router
from ..{{ cookiecutter.app_name }}.views import router as {{ cookiecutter.app_name }}_router
from ..base.exceptions import ServiceUnavailableError, BusinessError

api = NinjaAPI(
    csrf=True,
    title="🥷 {{cookiecutter.project_name}}",
    description="{{cookiecutter.description}}",
)

api.add_router("/", base_router, tags=["base"])
api.add_router("/accounts/", accounts_router, tags=["accounts"])
api.add_router("/{{ cookiecutter.app_name }}/", {{ cookiecutter.app_name }}_router, auth=django_auth, tags=["{{ cookiecutter.app_name }}"])


@api.exception_handler(ValidationError)
def validation_errors(request, exc):
    def parse_input_validation(error):
        field = ".".join(error.get("loc"))
        return f"{field}: {error.get('msg')} ({error.get('type')})"

    error = ""
    if len(exc.errors) >= 1:
        error = parse_input_validation(exc.errors[0])
    return JsonResponse({"message": f"[INVALID INPUT] {error}"}, status=422)


@api.exception_handler(ServiceUnavailableError)
def service_unavailable_errors(request, exc):
    error = str(exc)
    return JsonResponse(
        {
            "message": f"[UNAVAILABLE] Me desculpe! Serviço não disponível no momento. Tente mais tarde: {error}"
        },
        status=503,
    )


@api.exception_handler(BusinessError)
def business_errors(request, exc):
    error = str(exc)
    return JsonResponse({"message": f"[ERROR] {error}"}, status=400)
