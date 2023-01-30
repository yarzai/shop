from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    # binray = models.BinaryField(max_length=20, null=True, editable=True)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "product"


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "category"
