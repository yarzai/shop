from products.forms import ProductModalForm
from django.shortcuts import render,  redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


from products.models import Product, Category


class AboutView(View):
    def get(self, request, **kwargs):
        print(kwargs)
        # form = TestForm(initial={'name': 'Test', "age": 34})
        form = ProductModalForm()
        return render(request, 'index.html', {"form": form, **kwargs})

    def post(self, request):
        # form = TestForm(request.POST)
        form = ProductModalForm(request.POST, request.FILES)
        if form.is_valid():
            res = form.save()
            return redirect(reverse_lazy("products:detail", args=[res.id]))
        else:
            print(form.errors)
            return render(request, 'about.html', {"form": form})


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'products/list_products.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    queryset = Product.objects.all()
    fields = "__all__"
    template_name = 'products/create_product.html'


class ListProductView(View):
    def get(self, request, *args, **kwargs):
        print(dict(request.session))
        # products = Product.db.is_available()
        categories = Category.objects.all()
        return render(request, "products/list_products.html", {"categories": categories})


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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    pk_url_kwarg = 'prod_id'


class ProductUpdateView(UpdateView):
    model = Product
    # fields = '__all__'
    fields = ['title', 'price']
    pk_url_kwarg = 'prod_id'
    template_name = 'products/product_update.html'


class ProductDeleteView(DeleteView):
    model = Product
    pk_url_kwarg = 'prod_id'
    success_url = reverse_lazy("products:list")
