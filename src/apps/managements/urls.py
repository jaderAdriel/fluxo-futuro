from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list-managements"),
    path('create/', views.create, name="create-management"),
    path('<int:id>/detail/', views.detail, name="detail-management"),
    path('<int:id>/edit/', views.edit, name="edit-management"),
    path('<int:id>/delete/', views.delete, name="delete-management")
]
