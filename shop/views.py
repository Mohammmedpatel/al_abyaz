from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    featured_products = Product.objects.filter(available=True, is_featured=True)[:4]
    bestseller_products = Product.objects.filter(available=True, is_bestseller=True)[:4]
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'featured_products': featured_products,
        'bestseller_products': bestseller_products,
        'whatsapp_number': settings.WHATSAPP_NUMBER,
        'upi_id': settings.UPI_ID,
        'shop_name': settings.SHOP_NAME,
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category, available=True).exclude(id=id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
        'whatsapp_number': settings.WHATSAPP_NUMBER,
        'upi_id': settings.UPI_ID,
        'shop_name': settings.SHOP_NAME,
    }
    return render(request, 'shop/product/detail.html', context)


def about(request):
    context = {
        'whatsapp_number': settings.WHATSAPP_NUMBER,
        'upi_id': settings.UPI_ID,
        'shop_name': settings.SHOP_NAME,
    }
    return render(request, 'shop/about.html', context)


def contact(request):
    context = {
        'whatsapp_number': settings.WHATSAPP_NUMBER,
        'upi_id': settings.UPI_ID,
        'shop_name': settings.SHOP_NAME,
    }
    return render(request, 'shop/contact.html', context)
