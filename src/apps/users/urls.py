from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list-users"),
    path('create/', views.create, name="create-user"),
    path('<int:id>/detail/', views.detail, name="detail-user"),
    path('<int:id>/edit/', views.edit, name="edit-user"),
    path('<int:id>/delete/', views.delete, name="delete-user")
]
