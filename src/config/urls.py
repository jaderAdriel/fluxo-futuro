from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('access/', include("django.contrib.auth.urls")),  
    path('accounts/', include("apps.accounts.urls")),
]
