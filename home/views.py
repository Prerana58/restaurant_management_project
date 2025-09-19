from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, "home/about.html")

def index(request):
    restaurant_name=getattr(settings, "RESTAURANT_NAME", "My Restaurant")
    return render(request, "home/index.html", {"restaurant_name":restaurant_name})

def reservations(request):
    context={ "current_year": datetime.now().year}
    return render(request,'reservations.html', context)