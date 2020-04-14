from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from user import views


urlpatterns = [
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
    path("signup/", views.CreateUserViewSet.as_view(), name="signup-create")
]