from django.shortcuts import render

# Create your views here.

red_bali = {
    "description": "of Element Kratom as this Red Bali ignites your senses like a wildfire"
}

def home(request):
    return render(request, "home.html", {})

def products(request):
    return render(request, "products.html", {})

def product_page(request):
    return render(request, "product-page.html", {})

def kratom_overview(request):
    return render(request, "kratom-overview.html")