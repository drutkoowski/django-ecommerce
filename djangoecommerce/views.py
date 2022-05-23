from django.shortcuts import render
from store.models import Product, ReviewRating


def home(request):
    reviews = None
    products = Product.objects.all().filter(is_available=True).order_by("price")
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    context = {
        "products": products,
        "reviews": reviews,
    }
    return render(request, "home.html", context)
