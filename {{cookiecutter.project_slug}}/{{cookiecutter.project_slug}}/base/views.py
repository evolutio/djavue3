{% if cookiecutter.django_api == "django_ninja" %}
from ninja import Router, Schema

router = Router()


class Error(Schema):
    message: str


@router.get("/dapau", response={500: Error}){% endif %}
def dapau(request):
    raise Exception("break on purpose")
