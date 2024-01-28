from django.shortcuts import render
from django.http import HttpResponse

def ecommerce_index_view(request):
    return HttpResponse("Welcome to 6410742297 Kullaphat Kajhan views!")

def item_view(request, item_id):
    context_data = {
        "item_id": item_id
    }
    return render(request, 'index.html', context = context_data)


def home(request):
    return render(request, 'home.html')

def category(request):
    return render(request, 'category.html')

def product(request):
    return render(request, 'product.html')

def contact(request):
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')