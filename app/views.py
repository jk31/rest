from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response

from app.serializers import TaskSerializer
from app.models import Task

class Index(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response("lel")

    def post(self, request):
        res = request.data["key1"]
        res = 3*int(res)
        return Response(res)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
