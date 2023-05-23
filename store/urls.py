from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views
from store.views import signup
from django.contrib.auth import views as auth_views
from .forms import LoginForm


app_name = 'store'
## this is a test



urlpatterns = [

    path('', views.main, name="main"),
    path('cart/', views.cart, name="cart"),
    path('contact/', views.contact, name="contact"),
    path('store/', views.store, name="store"),
    path('second_shop/', views.second_shop, name="second_shop"),
    path('checkout/', views.checkout, name="checkout"),
    path('items/',include('item.urls')),
    path('base/', views.base, name="base"),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
