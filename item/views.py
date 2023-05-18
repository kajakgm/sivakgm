from django.shortcuts import render, get_object_or_404
from .models import Item

def item_list(request):
    items = Item.objects.all()  # Retrieve all items from the database
    context = {'items': items}
    return render(request, 'store.html', context)



def product_list(request):
    # Your view logic here
    return render(request, 'item/product_list.html')

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/detail.html', {
        'item': item,

    })
