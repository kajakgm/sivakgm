from django.shortcuts import render,redirect
from item.models import Category, Item
from .forms import SignupForm

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
    
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    context={'categories': categories, 'items': items}
    return render(request, 'store/store.html', context)
def base(request):
    context = {}
    return render(request, 'store/base.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)


def second_shop(request):
    context = {}
    return render(request, 'store/second_shop.html', context)



