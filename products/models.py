from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
