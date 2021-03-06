from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def add_to_cart(self):
        return reverse('shop:add-to-cart', kwargs={
            'slug': self.slug
        })

    def order(self):
        return reverse('shop:order', kwargs={
            'slug': self.slug
        })


class ProductOrder(models.Model):
    productname = models.CharField(max_length=100, db_index=True)
    userfirstname = models.CharField(max_length=100, db_index=True)
    userlastname = models.CharField(max_length=100, db_index=True)
    usercontact = models.CharField(max_length=100, db_index=True)
    useremail = models.CharField(max_length=100, db_index=True)
    country = models.CharField(max_length=100 , db_index=True)
    useraddressline1 = models.CharField(max_length=100, db_index=True)
    useraddressline2 = models.CharField(max_length=100, db_index=True)
    city = models.CharField(max_length=50 , db_index=True)
    userpincode = models.CharField(max_length=100, db_index=True)
    note = models.TextField(max_length=500 , db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.productname