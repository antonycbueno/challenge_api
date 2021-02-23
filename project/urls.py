from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

from api.viewset import ProductViewSet, ClientViewSet, FavoriteViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'favorites', FavoriteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]