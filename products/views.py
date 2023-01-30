from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product

# Create your views here.


# @login_required(login_url="/admin/login")
@login_required
def welcome(request):

    # return HttpResponse("<h1>Hi</h1>")
    val = "Hi"
    print(dir(request))
    print(request.user)

    return render(request, 'products/welcome.html', {"result": val, "test": 12})


def create_product(request):
    if request.method == 'GET':
        return render(request, "products/create_product.html")
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        is_avaliable = request.POST.get("is_avaliable")

        # if is_avaliable:
        #     is_avaliable = True
        # else:
        #     is_avaliable = False

        product = Product.objects.create(title=title, price=price,
                                         is_avaliable=bool(is_avaliable))
        return render(request, "products/create_product.html", {"id": product.id})


def list_products(request):
    products = Product.objects.all()
    print(products)
    return render(request, "products/list_products.html", {"products": products})


def product_detail(request, prod_id):
    product = Product.objects.get(id=prod_id)
    return render(request, 'products/product-detail.html', {"product": product})


def product_delete(request, prod_id):
    product = Product.objects.get(id=prod_id)
    product.delete()

    return redirect("/products")
