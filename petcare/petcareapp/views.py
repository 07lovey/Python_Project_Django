


from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import services as service
from . models import Blogs as blog
from . models import BookNowForm
from . models import ContactForm
from . models import FoodCare as FC
from . serializers import servicesSerializers,BlogsSerializers,FoodCareSerializers
import requests
from django.contrib import messages

class servicesList(APIView):
    def get(self,reqeust):
        services1=service.objects.all()
        serializer=servicesSerializers(services1, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class BlogsList(APIView):
    def get(self,reqeust):
        blogs1=blog.objects.all()
        serializer=BlogsSerializers(blogs1, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class FoodCareList(APIView):
    def get(self,reqeust):
        FC1=FC.objects.all()
        serializer=BlogsSerializers(FC1, many=True)
        return Response(serializer.data)
    def post(self):
        pass

# Create your views here.
def home(request):
    response=requests.get('http://127.0.0.1:8000/serviceslist/').json()
    response2=requests.get('http://127.0.0.1:8000/blogslist/').json()
    response3=requests.get('http://127.0.0.1:8000/foodcarelist/').json()
    return render(request,"index.html",{'response':response,'response2':response2,'response3':response3})  

def booknowform(request):
        if request.method == "POST":
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            emailid=request.POST.get('emailid')
            phoneno=request.POST.get('phoneno')
            address=request.POST.get('address')
            en= BookNowForm(firstname=firstname,lastname=lastname,email_id=emailid,phone_no=phoneno,address=address)
            en.save()
            messages.success(request, 'Booking Confirmed! successfully.')
        return render(request,"booknowform.html",{})    
def services(request):
    response=requests.get('http://127.0.0.1:8000/serviceslist/').json()
    return render(request,"services.html",{'response':response})
def blogs(request):
    response=requests.get('http://127.0.0.1:8000/blogslist/').json()
    return render(request,"blogs.html",{'response':response})
def foodCare(request):
    response=requests.get('http://127.0.0.1:8000/foodcarelist/').json()
    return render(request,"foodcare.html",{'response':response})
def contact(request):
    if request.method == "POST":
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            emailid=request.POST.get('emailid')
            phoneno=request.POST.get('phoneno')
            address=request.POST.get('address')
            en= ContactForm(firstname=firstname,lastname=lastname,email_id=emailid,phone_no=phoneno,address=address)
            en.save()
            messages.success(request, 'Contact form submitted successfully.')
    return render(request,"contact.html")
          
