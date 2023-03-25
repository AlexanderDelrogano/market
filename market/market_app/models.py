from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    info = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', default="images/noimage.jpg")
    categories = models.ManyToManyField("Category", blank=True, related_name="products")

    def get_absolute_url(self):
        return reverse("product_detail_url", kwargs={'id': self.id})

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def get_absolute_url(self):
        return reverse("category_detail_url", kwargs={'id': self.id})
    
    def __str__(self):
        return self.title
    
class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=40)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.name