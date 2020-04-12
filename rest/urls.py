from django.contrib import admin
from django.urls import path, include

import app.views

urlpatterns = [
    path("", app.views.index, name="index"),
    path('admin/', admin.site.urls),
]
