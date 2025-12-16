from django.urls import path
from . import views

urlpatterns = [
    path('/', views.teste),
    path('user/<int:user_id>/', views.get_user),
    path('user/<user_id>/delete', views.delete_user)
]