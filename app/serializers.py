from rest_framework import serializers
from app.models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Task
        fields = ["owner", "title", "created", "description"]
        read_only_fields = ["owner", "created"]