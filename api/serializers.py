from rest_framework import serializers

from .models import Product, Client, Favorite


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'