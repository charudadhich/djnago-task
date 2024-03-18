from rest_framework.response import Response
from demo.exceptions import ApiException
from .constants import Constant


class Responder:

    @classmethod
    def send(cls, code, data=None, count=None, status=True):
        return Response(
            {
                "status": status,
                "code": code,
                "message": Constant.response_messages[code],
                "data": data
            },
            status=200 if status else 400
        )

    @staticmethod
    def throw_error(code):
        raise ApiException(code)
