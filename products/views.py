from products.forms import TestForm
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic.base import View, TemplateView

from products.models import Product

# Create your views here.


# @login_required(login_url="/admin/login")
# @login_required
def welcome(request):

    # return HttpResponse("<h1>Hi</h1>")
    # val = "Hi"
    # print(dir(request))
    # print(request.user)

    # return render(request, 'products/welcome.html', {"result": val, "test": 12})

    return redirect(reverse_lazy("products:list"))


def create_product(request):
    if request.method == 'GET':
        return render(request, "products/create_product.html")
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        is_available = request.POST.get("is_available")

        # if is_avaliable:
        #     is_avaliable = True
        # else:
        #     is_avaliable = False

        product = Product.objects.create(title=title, price=price,
                                         is_available=bool(is_available))
        return render(request, "products/create_product.html", {"id": product.id})


class CreatProductView(View):
    def get(self, request):
        return render(request, "products/create_product.html")

    def post(self, request):
        title = request.POST.get("title")
        price = request.POST.get("price")
        is_available = request.POST.get("is_available")
        product = Product.objects.create(title=title, price=price,
                                         is_available=bool(is_available))
        return render(request, "products/create_product.html", {"id": product.id})


def list_products(request):
    products = Product.db.is_available()
    # products = Product.objects.filter(Q(is_available=True) | Q(price__lt=500))
    # products = Product.objects.filter(title__icontains='p')
    # products = Product.objects.filter(title__istartswith='p')
    # products = Product.objects.all().order_by("-price")
    print(products.query)
    return render(request, "products/list_products.html", {"products": products})


class ListProductView(View):
    def get(self, request, *args, **kwargs):
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


class AboutView(View):
    def get(self, request):
        form = TestForm(initial={'name': 'Test', "age": 34})
        return render(request, 'about.html', {"form": form})

    def post(self, request):
        form = TestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
            return render(request, 'about.html', {"form": form})
