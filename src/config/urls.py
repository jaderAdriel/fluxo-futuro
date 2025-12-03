from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('access/', include("django.contrib.auth.urls")),  
    path('', include("apps.dashboard.urls")),
    path('managements/', include("apps.managements.urls")),
    path('finance/', include("apps.finance.urls")),
    path('events/', include("apps.events.urls")),
    path('meetings/', include("apps.meetings.urls")),
    path('permissions/', include("apps.permissions.urls")),
]
