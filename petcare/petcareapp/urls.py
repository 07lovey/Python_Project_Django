from urllib import request
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="index"),
    path('home/',views.home,name="home"),
    path("booknowform/",views.booknowform,name="booknowform"),
    path('services/',views.services,name="services"),
    path('blogs/',views.blogs,name="blogs"),
    path('foodcare/',views.foodCare,name="foodcare"),
    path('contact/',views.contact,name="contact"),
]
