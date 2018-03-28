from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from reviews.forms import ReviewForm

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products/product-list.html", {'products': products})    
    
def product_item(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ReviewForm()
    return render(request, "products/product-item.html", {'product': product, 'review_form': form })

def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query)
    return render(request, "products/product-list.html", {'products': products})    
    
    