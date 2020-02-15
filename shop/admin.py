from django.contrib import admin
from .models import   Category  , Product  ,Liteorder
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Liteorder)
