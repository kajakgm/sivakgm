from django.shortcuts import render,redirect
from item.models import Category, Item , Order , OrderItem , Customer
from .forms import SignupForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'store/signup.html', {
        'form': form
    })


def main(request):

    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, 'store/main.html', {
        'categories': categories,
        'items': items})

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0}
        cartItems = order['get_cart_items']
    
    items = Item.objects.filter(is_sold=False).exclude(category_id=4)
    categories = Category.objects.all()
    context={'categories': categories, 'items': items, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def base(request):
    context = {}
    return render(request, 'store/base.html', context)


# views.py (or any other file where you want to send the email)

from django.core.mail import send_mail

def send_email(request):
    subject = 'Hello from Django'
    message = 'This is a test email sent using Django.'
    from_email = 'petsum43@gmail.com'
    recipient_list = []
    
    send_mail(subject, message, from_email, recipient_list)



def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)


def second_shop(request):
    items = Item.objects.filter(is_sold=False,category_id=4)
    categories = Category.objects.all()
    context={'categories': categories, 'items': items,}
    return render(request, 'store/second_shop.html', context)
    

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0}
        
    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)
