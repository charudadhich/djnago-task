from rest_framework.views import APIView
from .serializers import BaseSerializer
from utils.responder import Responder


class BaseView(APIView):
    def post(self, request):
        serializer = BaseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        data = serializer.data
        print("done")
        return Responder.send(201, data)