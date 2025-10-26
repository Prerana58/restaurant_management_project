from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer
from .serializers import MenuItemSerializer

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
    
class MenuCategoryListView:
    queryset=MenuCategory.objects.all()
    serializer_class=MenuCategorySerializer

class FeaturedMenuItemsView(generics.ListAPIView):
    serializer_class=MenuItemSerializer
    def get_queryset(self):
        return MenuItem.objects.filter(is_featured=True, is_available=True)


