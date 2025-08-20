from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, "home/about.html")

def home(request):
    restaurant=Restaurant.objects.first()
    context={
        "restaurant_name":
        restaurant.name if restaurant else "Our Restaurant"
    }
    return render(request, "home/index.html", context)