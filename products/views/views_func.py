from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from products.models import Product

# Create your views here.


def welcome(request):
    return redirect(reverse_lazy("products:list"))


def create_product(request):
    if request.method == 'GET':
        return render(request, "products/create_product.html")
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        is_available = request.POST.get("is_available")
        product = Product.objects.create(title=title, price=price,
                                         is_available=bool(is_available))
        return render(request, "products/create_product.html", {"id": product.id})


def list_products(request):
    # print(dir(request))
    print("P", request.GET.get("p"))
    print("N", request.GET.get("n"))
    products = Product.db.is_available()
    return render(request, "products/list_products.html", {"products": products})


def product_detail(request, prod_id):
    product = Product.objects.get(id=prod_id)
    print(product.tax)
    return render(request, 'products/product-detail.html', {"product": product})


def product_delete(request, prod_id):
    product = Product.objects.get(id=prod_id)
    product.delete()

    return redirect(reverse_lazy("products:list"))


def product_update(request, prod_id):
    product = Product.objects.get(id=prod_id)
    if request.method == 'GET':
        return render(request, 'products/product_update.html', {"product": product})
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        is_avaliable = request.POST.get("is_avaliable")
        desc = request.POST.get("desc")

        product.title = title
        product.price = price
        product.is_available = bool(is_avaliable)
        product.description = desc

        product.save()

        return redirect(reverse_lazy("products:update", args=[product.id]))
