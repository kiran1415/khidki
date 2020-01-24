from __future__ import unicode_literals
from django.db import models
from django.conf import  settings
from accounts.models import  Profile
from shop.models import  Product

# Create your models here


class CartItem(models.Model):
    product = models.ManyToManyField(Product, blank=True)
    ordered = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)



    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_item_price(self):
        return self.quantity * self.product.price




