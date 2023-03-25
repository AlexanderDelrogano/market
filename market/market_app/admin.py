from django.contrib import admin
from .models import Product, Category, Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'product']


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)