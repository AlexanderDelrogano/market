from django.urls import path
from .views import *


urlpatterns = [
    path('', product_list, name='product_list_url'),
    path('categories/', category_list, name='categories_url'),
    path('product/<int:id>/', product_detail, name="product_detail_url"),
    path('categories/<int:id>/', category_detail, name="category_detail_url"),
    path('save_order', save_order)
]
