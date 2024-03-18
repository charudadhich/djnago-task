import traceback
from rest_framework.decorators import api_view
from django.conf import settings
from django.urls.exceptions import Resolver404
from rest_framework.exceptions import (
    MethodNotAllowed,
    ParseError,
    UnsupportedMediaType,
    NotAuthenticated,
    AuthenticationFailed,
    PermissionDenied,
    ValidationError as DRFValidationError,
    Throttled,
)

from demo.exceptions import ApiException
from utils.responder import Responder
from utils.constants import Constant

def handle_errors(exception, context):
    error_mappings = {
        ApiException: lambda ex: handle_api_exception(ex),
        MethodNotAllowed: 505,
        Resolver404: 501,
        ParseError: 502,
        PermissionDenied: 506,
        Throttled: 510,
        UnsupportedMediaType: 503,
        NotAuthenticated: 504,
        AuthenticationFailed: 504,
        DRFValidationError: lambda ex: handle_validation_error(ex),
    }
    response_code = error_mappings.get(type(exception), 500)
    if callable(response_code):
        response_code = response_code(exception)

    if response_code == 500:
        if settings.DEBUG:
            raise exception
    return Responder.send(response_code, status=False)


def handle_api_exception(exception):
    return exception.error_code


def handle_validation_error(exception):
    response_code = exception.get_codes()
    while isinstance(response_code, dict):
        response_code = list(response_code.values())[0]
    if isinstance(response_code, list):
        response_code = response_code[0]
    if isinstance(response_code, str):
        response_code = Constant.django_default_codes.get(response_code, 507)
    return response_code


@api_view(("GET",))
def handler404(request, exception):
    return Responder.send(501, status=False)
