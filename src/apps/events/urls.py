from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_events, name="list-events"),
    path('create/', views.create_event, name="create-event"),
    path('<int:id>/edit/', views.edit_event, name="edit-event"),
    path('<int:id>/delete/', views.delete_event, name="delete-event"),
    path('<int:id>/detail/', views.detail_event, name="detail-event"),
]
