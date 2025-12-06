from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list-departments"),
    path('create/', views.create, name="create-department"),
    path('<int:id>/detail/', views.detail, name="detail-department"),
    path('<int:id>/edit/', views.edit, name="edit-department"),
    path('<int:id>/delete/', views.delete, name="delete-department")
]
