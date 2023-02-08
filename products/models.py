from django.db import models
from django.forms import ValidationError
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from utility.slugHelper import unique_slug_generator


# Create your models here.

CATEGORIES = (
    ("ph", 'Phone'),
    ("cm", 'Camera')
)


def price_gt_500(value):
    if value < 500:
        raise ValidationError("Please enter above 500.")


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
    category = models.CharField(max_length=50, choices=CATEGORIES, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def tax(self):
        return self.price * 0.1

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
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


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "category"
