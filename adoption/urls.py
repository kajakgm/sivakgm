
from django.contrib import admin
from django.urls import path, include
from item.views import item_list
from item.views import product_list


urlpatterns = [

    path('', include('store.urls')),
    path('',include('item.urls')),
    path('items/', item_list, name='item_list'),
    path('products/', product_list, name='product_list'),
    path('admin/', admin.site.urls)

]

