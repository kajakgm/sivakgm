from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views


app_name = 'adoption'


urlpatterns = [

    path('', views.main, name="main"),
    path('cart/', views.cart, name="cart"),
    path('contact/', views.contact, name="contact"),
    path('store/', views.store, name="store"),
    path('second_shop/', views.second_shop, name="second_shop"),
    path('checkout/', views.checkout, name="checkout"),
    path('items/',include('item.urls')),
    path('base/', views.base, name="base"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
