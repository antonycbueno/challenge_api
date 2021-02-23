from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    product_id = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("api:detail", kwargs={"product_id": self.product_id})


class Client(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    name = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name