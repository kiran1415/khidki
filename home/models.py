from django.db import models

# Create your models here.
class Terms(models.Model):
    heading = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)

    def __str__(self):
        return self.heading