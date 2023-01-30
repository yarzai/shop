
from django.contrib import admin
from django.urls import path, include
from products.views import welcome


urlpatterns = [
    path('admin/', admin.site.urls),
    path("welcome/", welcome),
    path("products/", include("products.urls"))
]
