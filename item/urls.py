from django.urls import path
from . import views
from item.views import item_list
from item.views import product_list

app_name = 'item'

urlpatterns = [
    path('items/', views.items, name='items'),
    path('<int:pk>/', views.detail, name='detail'),
    path('items/', item_list, name='item_list'),
    path('products/', product_list, name='product_list'),


]