from django.urls import path
from .views import telegram_login,product_list

urlpatterns = [
    path('api/login/', telegram_login, name='telegram-login'),
    path('', product_list, name='product_list')
]
