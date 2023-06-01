from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Item, Category , Order , OrderItem, Customer
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

def items(request):
    query = request.GET.get('query','')
    category_id = request.GET.get('category' , 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items':  items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
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






def updateItem(request):
	data = json.loads(request.body)
	itemId = data['itemId']
	action = data['action']
	print('Action:', action)
	print('Item:', itemId)

	customer = request.user.customer
	item = Item.objects.get(id=itemId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, item=item)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Customer

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a Customer object and associate it with the user
            customer = Customer.objects.create(user=user, name=user.username, email=user.email)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
