from django.shortcuts import render
from home.models import Product


def example(request):
    phone = Product.objects.all()
    context = {
        'phone': phone
    }
    return render(request, 'index.html', context)