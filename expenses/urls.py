from django.urls import path
from .views import create_user, add_expense, get_user_expenses, get_user_balances

urlpatterns = [
    path('api/users/', create_user, name='create_user'),
    path('api/expenses/', add_expense, name='add_expense'),
    path('api/users/<int:user_id>/expenses/', get_user_expenses, name='get_user_expenses'),
    path('api/users/<int:user_id>/balances/', get_user_balances, name='get_user_balances'),
]
