from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_transaction, name='add'),
    path('delete/<int:pk>/', views.delete_transaction, name='delete'),
]
