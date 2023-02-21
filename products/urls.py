
from django.urls import path
from products.views.views_func import (
    create_product,
    list_products,
    product_detail,
    product_delete,
    product_update,
)
from products.views.views_class import (
    ListProductView,
    CreatProductView,
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView
)

app_name = 'products'

urlpatterns = [
    path("", ListProductView.as_view(), name="list"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("detail/<int:prod_id>/",
         product_detail, name="detail"),
    path("delete/<int:prod_id>", ProductDeleteView.as_view(), name="delete"),
    path("update/<int:prod_id>", product_update, name="update"),
]
