from django.urls import path

import store.urls
from . import views

urlpatterns = [

    path('', views.main, name="main"),
    path('cart/', views.cart, name="cart"),
    path('contact/', views.contact, name="contact"),
    path('store/', views.store, name="store"),
    path('second_shop/', views.second_shop, name="second_shop"),
    path('checkout/', views.checkout, name="checkout"),
]
