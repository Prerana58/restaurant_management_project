from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    context={
        "restaurant_name":settings.RESTAURANT_NAME,
        "restaurant_phone":settings.RESTAURANT_PHONE,
    }
    return render(request, "home/index.html", context)
    
def about(request):
    return render(request, "home/about.html")

def contact(request):
    restaurant_name=getattr(settings, "RESTAURANT_NAME", "My Restaurant")
    return render(request, "home/contact.html", {"restaurant_name":restaurant_name})

def menu_view(request):
    menu_items=[
        {"name":"Margherita Pizza", "price":"250Rs",
        "description":"Classic cheese pizza with tomato souce."},
        {"name":"Paneer Tikka", "price":"300Rs", 
        "description":"Grilled paneer cubes marinated in spices."},
        {"name":"Veg Biryani", "price":"220Rs",
        "description":"Aeomatic rice with vegetables and spices."},
        {"name":"Pasta Alfredo", "price":"280Rs",
        "description":"Creamy White Sauce pasta with herbs."},
    ]
    return render(request, "home/menu.html", {"menu_items":menu_items})