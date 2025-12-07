from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('health/', views.health),
    path('admin/', admin.site.urls),
    path('access/', include("django.contrib.auth.urls")),  
    path('', include("apps.dashboard.urls")),
    path('users/', include("apps.users.urls")),
    path('departments/', include("apps.departments.urls")),
    path('finance/', include("apps.finance.urls")),
    path('events/', include("apps.events.urls")),
    path('meetings/', include("apps.meetings.urls")),
    path('events/', include('apps.events.urls'))
]
