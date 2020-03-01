from django.db import models

# Create your models here.
from django.db import models
import datetime

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)