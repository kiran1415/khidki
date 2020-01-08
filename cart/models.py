from __future__ import unicode_literals
from django.db import models
from accounts.models import  Profile
from shop.models import  Product

# Create your models here


class OrderItem(models.Model):
    product = models.OneToOneField(Product , on_delete=models.SET_NULL , null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    data_ordered = models.DateTimeField(null=True)


    def __str__(self):
        return self.product.name


