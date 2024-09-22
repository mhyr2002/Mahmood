from django.urls import path
from . views import *

app_name='shop'

urlpatterns = [

    path('products/',product_list,name='product_list'),
    path('products/<slug:category_slug>',product_list,name='product_list_by_category'),
    path('product_detail/<int:id>/<slug:slug>/',product_detail,name='product_detail')

]