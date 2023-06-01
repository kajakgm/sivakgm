from django.urls import path
from . import views
from item.views import *


app_name = 'item'

urlpatterns = [
    path('items/', views.items, name='items'),
    path('<int:pk>/', views.detail, name='detail'),
    path('items/', item_list, name='item_list'),
    path('products/', product_list, name='product_list'),
    path('update_item/', views.updateItem, name="update_item"),


]