from django.db import models

# Create your models here.


class User(models.Model):
    


    ROLES = (('client','Client'),
             ('seller','Seller'),
             ('courier','Courier'),
             ('admin','Admin'),
             )
    
    telegram_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=20,blank=True)
    phone_number = models.TextField(max_length=15,blank=True)
    role = models.CharField(max_length=10,choices=ROLES,default='client')
    address = models.CharField(max_length=50,blank=True)






