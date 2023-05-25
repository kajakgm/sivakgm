from django.shortcuts import render, get_object_or_404
from .models import Item, Category
import json
from django.views.generic import ListView


def items(request):
    query = request.GET.get('query','')
    items = Item.objects.filter(is_sold=False)

    if query:
        items = items.filter(name__icontains=query)

    return render(request, 'item/items.html', {
        'items':  items,
        'query': query,
    })



def item_list(request):
    items = Item.objects.all()
    
    context = {'items': items,
                }
    return render(request, 'store.html', context)





def product_list(request):
    # Your view logic here
    return render(request, 'item/product_list.html')

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/detail.html', {
        'item': item,

    })

