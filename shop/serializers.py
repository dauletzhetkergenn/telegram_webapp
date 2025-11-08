from rest_framework import serializers
from .models import Product,Order,OrderItem
from delivery.models import Delivery
from users.models import User



class ProductSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField(source = 'shop.name',read_only=True)

    class Meta:
        model = Product
        fields = ['id','title','description','price']



class OrderItemSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = OrderItem
        fields = ['id','product','quantity']


class DeliverySerializer(serializers.ModelSerializer):


    class Meta:
        model = Delivery
        fields = ['id','order','courier','status','address','created_at']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    delivery = DeliverySerializer(read_only=True)
    class Meta:
        model = Order
        fields = ['id','shop','client','price','items','delivery','status','created_at','updated_at']
