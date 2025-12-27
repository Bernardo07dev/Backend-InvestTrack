from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.verify),
    path('create/', views.create_user),
    path('user/<int:user_id>/', views.get_user),
    path('investimentos/', views.create_investimento),
    path('get-investimentos/', views.get_investimentos),
    path('transaction/', views.create_transaction),
    path('carteira/', views.get_carteira),
    path('delete_invest/', views.delete_invest),
    path('diminui_invest/', views.diminui_invest)
]