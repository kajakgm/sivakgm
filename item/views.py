from django.shortcuts import render

from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()  # Retrieve all items from the database
    context = {'items': items}
    return render(request, 'store.html', context)

