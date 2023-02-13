import random
from django.db import models
from django.forms import ValidationError
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from utility.slugHelper import unique_slug_generator
import os
from shop import settings


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class ProductModalManger(models.Manager):
    # def all(self):
    #     return self.filter(is_available=True)

    def is_available(self):
        return self.filter(is_available=True)


# Create your models here.
CATEGORIES = (
    ("ph", 'Phone'),
    ("cm", 'Camera')
)


def price_gt_500(value):
    if value < 500:
        raise ValidationError("Please enter above 500.")


def file(instance, filename):
    print(filename)
    ext = filename.split(".")[1]
    return f"products/{random.randint(1,99999)}.{ext}"


def image_validator(image):
    # if (image.size > 20000):
    #     raise ValidationError("Image must be less than 20KB.")
    pass


class Product(models.Model):
    title = models.CharField(max_length=150, unique=True, error_messages={
        "unique": "No Duplicates.",
        "null": "please fill the input"
    }, help_text="Please enter a unique value.",)
    slug = models.SlugField(null=True, blank=True)
    price = models.IntegerField(validators=[price_gt_500])
    # binray = models.BinaryField(max_length=20, null=True, editable=True)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(
        Category, null=True)
    image = models.ImageField(
        upload_to=file, null=True, blank=True, validators=[image_validator])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    db = ProductModalManger()
    objects = ProductModalManger()

    @property
    def tax(self):
        return self.price * 0.1

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # if os.path.exists(self.image.path):
        #     os.remove(self.image.path)
        self.image.delete()
        return super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.price = int(self.price)
        if not self.id:
            self.price = self.price + self.price * 0.02
        print("Save Called")
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "product"


# def pre_save_product_signal(sender, instance, *arg, **kwargs):
#     print("Product pre_save")
#     instance.slug = unique_slug_generator(instance)

#     print(unique_slug_generator(instance))


# pre_save.connect(pre_save_product_signal, sender=Product)

def post_save_product_signal(sender, instance, created, *arg, **kwargs):
    print("Product post_save")
    if created:
        instance.slug = unique_slug_generator(instance)
        instance.save()


post_save.connect(post_save_product_signal, sender=Product)
