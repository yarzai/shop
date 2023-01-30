
from django.urls import path
from products.views import create_product, list_products, product_detail, product_delete


urlpatterns = [
    path("", list_products),
    path("create/", create_product),
    path("detail/<int:prod_id>", product_detail),
    path("delete/<int:prod_id>", product_delete),
]
