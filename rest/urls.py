from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("user/", include("user.urls")),
    path("app/", include("app.urls")),
    path('admin/', admin.site.urls),
    path("api-token-auth/", obtain_auth_token, name="api-token-auth")
]
