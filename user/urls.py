from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views


urlpatterns = [
    path("signup/", views.CreateUserViewSet.as_view(), name="signup-create")
]