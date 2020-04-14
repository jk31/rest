from django.urls import path, include
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from user import views


urlpatterns = [
    url(r"^auth/", include("djoser.urls")),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^auth/users/activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.UserActivationView.as_view()),
    url(r'^auth/users/password/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.ResetPasswordConfirmView.as_view()),
]