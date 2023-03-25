from django.shortcuts import render
from .models import Product, Category, Order
from django.http import HttpResponse
# Create your views here.

def build_menu(list, colls):
    return [list[i:i+colls] for i in range(0, len(list), colls)]

def product_list (request):
    products = Product.objects.all()
    return render(request, 'market_app/product_list.html', context={'product_block': build_menu(products, 3)})


def category_list(request):
    categories = Category.objects.all()
    return render(request, "market_app/categories.html", context={'categories': categories})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "market_app/product_detail.html", context={"product": product})

def category_detail(request, id):
    category = Category.objects.get(id=id)
    products = category.products.all()
    return render(request, "market_app/product_list.html", context={'product_block': build_menu(products, 3)})

def save_order(request):
        product = Product.objects.get(id = request.POST['product_id'])
        order = Order()
        order.name = request.POST['username']
        order.email = request.POST['useremail']
        order.product = product
        order.save()
        return render(request, 'market_app/order.html', context={'product': product, 'username': order.name})

