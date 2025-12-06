from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list-events'),
    path('create/', views.create_event, name='create-event'),
    path('edit/<int:pk>/', views.edit_event, name='edit-event'),
    path('delete/<int:pk>/', views.delete_event, name='delete-event'),
]
