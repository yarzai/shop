
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views.api import test, products, Products, ProductModalViewSet

router = DefaultRouter()
router.register("products", ProductModalViewSet)

app_name = 'products'

urlpatterns = [
    path("", products),
    path("", include(router.urls))
]
