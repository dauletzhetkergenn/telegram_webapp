from django.db import models
from shop.models import Order
from users.models import User
# Create your models here.
    

class Delivery(models.Model):
    order = models.OneToOneField(Order,related_name='delivery',on_delete=models.SET_NULL,null=True)
    courier = models.ForeignKey(User,related_name='deliveries',on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


