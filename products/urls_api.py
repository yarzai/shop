
from django.urls import path

from products.views.api import test

app_name = 'products'

urlpatterns = [
    path("", test),
]
