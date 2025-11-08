from django.shortcuts import render
from rest_framework import viewsets,permissions



from .models import Product,Shop,Order,OrderItem
from .serializers import ProductSerializer,OrderSerializer



class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny] 


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)