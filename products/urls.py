
from django.urls import path
from products.views import (
    create_product,
    list_products,
    product_detail,
    product_delete,
    product_update
)

app_name = 'products'

urlpatterns = [
    path("", list_products, name="list"),
    path("create/", create_product, name="create"),
    path("detail/<int:prod_id>", product_detail, name="detail"),
    path("delete/<int:prod_id>", product_delete, name="delete"),
    path("update/<int:prod_id>", product_update, name="update"),
]
