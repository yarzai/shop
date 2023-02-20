
from django.contrib import admin
from django.urls import path, include
from products.views.views_func import welcome
from django.conf import settings
from django.conf.urls.static import static
from products.views.views_class import AboutView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", welcome),
    path("products/", include("products.urls")),
    # path("about/", TemplateView.as_view(template_name="about.html",
    #      extra_context={'title': "from path"}))
    path("about/<int:test>/<str:name>", AboutView.as_view())
]

urlpatterns = urlpatterns + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
