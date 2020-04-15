from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from app.serializers import TaskSerializer
from app.permissions import OnlyOwnerGET
from app.models import Task

from django.core.mail import send_mail

class Index(APIView):
    """Example page"""
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response("lel")

    def post(self, request):
        res = request.data["key1"]
        res = 3*int(res)
        return Response(res)


class SendMail(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        send_mail("test subject", "test body", "myadress", ["recipient"])
        return Response("send mail")


class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for the Task model"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        return Task.objects.all().filter(owner=self.request.user)
        #return Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
