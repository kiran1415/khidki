from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.models import  Product
# Create your models here.


class Profile(models.Model):
    Male = 1
    Femal = 2
    Other = 3
    GENDER_CHOICES = (
        (Male, 'Male'),
        (Femal, 'Femal'),
        (Other, 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product ,  blank=True)
    mobile_no = models.CharField(max_length=12)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    shipping_address = models.CharField(max_length=300)
    billing_address = models.CharField(max_length=300)

    def __str__(self):
        return  self.user.username

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
