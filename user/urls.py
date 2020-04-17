from django.urls import path, include
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from user import views


urlpatterns = [
    url(r"^", include("djoser.urls")),
    url(r'^', include('djoser.urls.authtoken')),
    url(r'^users/activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.UserActivationView.as_view()),
    url(r'^users/password/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.ResetPasswordConfirmView.as_view()),
]