from django.urls import path
from rest_framework import routers


from .views import ProductListView, ProductDetailView


app_name = "api"

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:product_id>/', ProductDetailView.as_view(), name='detail'),
]