from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class Index(APIView):
    def get(self, request):
        return Response("lel")

    def post(self, request):
        res = request.data["key1"]
        res = 3*int(res)
        return Response(res)

