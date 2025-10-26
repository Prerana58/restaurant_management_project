from rest_framework import serializers
from .models import MenuCategory
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        fields=['name']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields=['id','name','description','price','is_available','is_featured']