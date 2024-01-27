from django.http import JsonResponse
from ..base.exceptions import BusinessError


class DjavueApiErrorHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exc):
        error = str(exc)
        if isinstance(exc, ValueError):
            response = JsonResponse({"message": f"[INVALID INPUT] {error}"}, status=422)
        elif isinstance(exc, BusinessError):
            response = JsonResponse({"message": f"[ERROR] {error}"}, status=400)
        else:
            response = JsonResponse({"message": f"[UNAVAILABLE] Me desculpe! Serviço não disponível no momento. Tente mais tarde: {error}"}, status=503)
        return response
