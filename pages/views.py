from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    context = {
        "DB": Products.objects.all()
    }
    return render(request, "pages/index.html", context)

def Product(request, id):
    context = {
        "DB": Products.objects.all(),
        "id": id
    }
    return render(request, "pages/product.html", context)