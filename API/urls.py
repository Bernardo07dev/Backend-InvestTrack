from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.verify),
    path('create/', views.create_user),
    path('user/<int:user_id>/', views.get_user),
    path('investimentos/', views.create_investimento)
]