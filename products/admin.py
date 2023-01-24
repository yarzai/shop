from django.contrib import admin
from products.models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', "is_avaliable", 'created']
    list_filter = ["title", 'is_avaliable', "created"]
    search_fields = ["title", 'price']
    date_hierarchy = "created"


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
