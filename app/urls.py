from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register(r"tasks", views.TaskViewSet)

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
    path("tasks/", include(router.urls))
]