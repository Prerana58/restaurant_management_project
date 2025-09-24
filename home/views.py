from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, "home/about.html")

def index(request):
    restaurant_name=getattr(settings, "RESTAURANT_NAME", "My Restaurant")
    return render(request, "home/index.html", {"restaurant_name":restaurant_name})

def reservations(request):
    try:
        context={ "current_year": datetime.now().year}
        return render(request,'reservations.html', context)
    except Exception as e:
        print(f"Error in reservations view: {e}")
        return HttpResponseSereverError("An error occured while loading he reservations page.")
    