from django.db import models
from django.forms import ValidationError

# Create your models here.

CATEGORIES = (
    ("ph", 'Phone'),
    ("cm", 'Camera')
)


def price_gt_500(value):
    if value < 500:
        raise ValidationError("Please enter above 500.")


class Product(models.Model):
    title = models.CharField(max_length=150, unique=True)
    price = models.IntegerField(validators=[price_gt_500])
    # binray = models.BinaryField(max_length=20, null=True, editable=True)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.price = self.price + self.price * 0.02
        print("Save Called")
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "product"


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "category"
