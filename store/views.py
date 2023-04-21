from django.shortcuts import render

def main(request):
    context = {}
    return render(request, 'store/main.html', context)

def store(request):
    context = {}
    return render(request, 'store/store.html', context)


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


