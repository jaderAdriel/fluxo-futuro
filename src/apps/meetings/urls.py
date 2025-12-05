from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list-meetings'),
    path('create/', views.create, name='create-meeting'),
    path('<int:id>/', views.detail, name='detail-meeting'),
    path('<int:id>/edit/', views.edit, name='edit-meeting'),
    path('<int:id>/delete/', views.delete, name='delete-meeting'),
]
