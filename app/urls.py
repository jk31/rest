from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
]