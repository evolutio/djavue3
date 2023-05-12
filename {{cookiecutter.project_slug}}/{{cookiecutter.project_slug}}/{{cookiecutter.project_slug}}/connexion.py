from django_connexion import DjangoApi as BaseDjangoApi


class _NullValidator:
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, view_func):
        return view_func


VALIDATOR_MAP = {
    'parameter': _NullValidator,
    'body': _NullValidator,
}


class DjangoApi(BaseDjangoApi):
    def __init__(self, *args, name='django_connexion', **kwargs):
        super().__init__(
            *args, name=name, validator_map=VALIDATOR_MAP, **kwargs
        )
