

from pickle import FALSE
from django.db import models

# Create your models here.
class services(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    brief_Desc=models.CharField(max_length=200)
    details=models.CharField(max_length=1000)
    
    def _str(self):
        return self.name
        
class BookNowForm(models.Model):
    firstname=models.CharField(max_length=20,null=False,blank=False)
    lastname=models.CharField(max_length=20,null=False,blank=False)
    email_id=models.EmailField(max_length=20,null=False,blank=False)
    phone_no=models.CharField(max_length=10,null=False,blank=False)
    address=models.CharField(max_length=100,null=False,blank=False)

class ContactForm(models.Model):
    firstname=models.CharField(max_length=20,null=False,blank=False)
    lastname=models.CharField(max_length=20,null=False,blank=False)
    email_id=models.EmailField(max_length=20,null=False,blank=False)
    phone_no=models.CharField(max_length=10,null=False,blank=False)
    address=models.CharField(max_length=100,null=False,blank=False)

class Blogs(models.Model):
    card_title=models.CharField(max_length=50,null=True)
    card_text=models.CharField(max_length=1000,null=True)
    card_link=models.CharField(max_length=500,null=True)

class FoodCare(models.Model):
    card_title=models.CharField(max_length=50,null=True)
    card_text=models.CharField(max_length=1000,null=True)
    card_link=models.CharField(max_length=500,null=True)

