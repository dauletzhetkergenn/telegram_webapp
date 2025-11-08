# users/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User 
from shop.models import Product
from rest_framework import status
from django.shortcuts import render

@api_view(['POST'])
def telegram_login(request):
    tg_data = request.data
    telegram_id = tg_data.get('id')
    
    if not telegram_id:
        return Response({'error': 'No telegram id'}, status=status.HTTP_400_BAD_REQUEST)
    
    user, created = User.objects.get_or_create(
        telegram_id=telegram_id,
        defaults={
            'name': tg_data.get('username'),
            'role': 'client',
        }
    )
    
    token, _ = Token.objects.get_or_create(user=user)
    
    return Response({'token': token.key, 'user_id': user.id, 'username': user.username})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})