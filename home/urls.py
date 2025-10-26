from django.urls import path
from .views import *

urlpatterns = [
    path('about/', views.about, name='about'),
    path('',views.home, name='home'),
    path("contact/", views.contact, name="contact"),
    path('menu-categories/',MenuCategoryListView.as_view(),name='menu-categories'),
]