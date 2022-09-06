
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from petcareapp import views
urlpatterns = [
    
    path("admin/", admin.site.urls),
    path('', include('petcareapp.urls')),
    path('serviceslist/',views.servicesList.as_view()),
    path('blogslist/',views.BlogsList.as_view()),
    path('foodcarelist/',views.FoodCareList.as_view()),
    # path('home/',views.home),
    # path('services',views.services),
    # path('booknowform/',views.booknowform),
    # path('blogs',views.blogs),
    # path('foodcare',views.foodCare),
    # path('contact',views.contact),
]
