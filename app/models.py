from django.db import models
from django.conf import settings

class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000)
    finished = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title