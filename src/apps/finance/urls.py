from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list-finances'),
    path('create/', views.create, name='create-finance'),
    path('<int:id>/', views.detail, name='detail-finance'),
    path('<int:id>/edit/', views.edit, name='edit-finance'),
    path('<int:id>/delete/', views.delete, name='delete-finance'),
]
