from django.db import models
from users.models import User

class Shop(models.Model):
    name = models.CharField(max_length=20,blank=False)
    owners = models.ManyToManyField(User,related_name='shops')


class Product(models.Model):
    shop = models.ForeignKey(Shop,related_name='products',on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=130)
    price = models.IntegerField()
    available = models.BooleanField(default=True)

class Cart(models.Model):
    client = models.ForeignKey(User,related_name='carts',on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,related_name='CartItems',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cart_products',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)



class Order(models.Model):

    STATUS = (('pending','Pending'),
              ('in_progress','In Progress'),
              ('delivering','Delivering'),
              ('delivered','Delivered'),
              ('canceled','Canceled'))
    


    shop = models.ForeignKey(Shop,related_name='orders',on_delete=models.SET_NULL,null=True)
    client = models.ForeignKey(User,related_name='client_orders',on_delete=models.SET_NULL,null=True)
    price = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,
                              choices=STATUS,default='pending')
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='orderItems',on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,related_name='productItem',on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1) 







