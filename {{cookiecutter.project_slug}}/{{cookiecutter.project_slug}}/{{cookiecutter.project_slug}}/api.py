from ninja import NinjaAPI
from ninja.security import django_auth

from ..base.views import router as base_router
from ..accounts.views import router as accounts_router
from ..{{ cookiecutter.app_name }}.views import router as {{ cookiecutter.app_name }}_router

api = NinjaAPI(
    csrf=True,
    title="🥷 {{cookiecutter.project_name}}",
    description="{{cookiecutter.description}}",
)

api.add_router("/", base_router, tags=["base"])
api.add_router("/accounts/", accounts_router, tags=["accounts"])
api.add_router("/{{ cookiecutter.app_name }}/", {{ cookiecutter.app_name }}_router, auth=django_auth, tags=["{{ cookiecutter.app_name }}"])
