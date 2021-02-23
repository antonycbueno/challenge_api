from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product
    slug_url_kwarg = 'product_id'
    slug_field = 'product_id'