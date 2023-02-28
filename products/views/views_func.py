from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required

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


# @login_required
def list_products(request):
    # print(dir(request))
    print("P", request.GET.get("p"))
    print("N", request.GET.get("n"))
    products = Product.db.is_available()
    return render(request, "products/list_products.html", {"products": products})


def product_detail(request, prod_id):
    try:
        product = Product.objects.get(id=prod_id)
    except Product.DoesNotExist:
        raise Http404()
        # return render(request, '404.html', {'P_not_found': True})
    # except Product.MultipleObjectsReturned
    # product = get_object_or_404(Product, id=prod_id)
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
        messages.warning(
            request, f"Product with id {prod_id} has been updated successfuly.")
        return redirect(reverse_lazy("products:update", args=[product.id]))
