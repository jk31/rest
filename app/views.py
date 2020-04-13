from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response

class Index(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response("lel")

    def post(self, request):
        res = request.data["key1"]
        res = 3*int(res)
        return Response(res)
