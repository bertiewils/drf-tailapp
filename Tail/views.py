from rest_framework.response import Response
from rest_framework.views import APIView


class Health(APIView):
    permission_classes = []

    def get(self, request, format=None):
        return Response(dict(status='OK'))
