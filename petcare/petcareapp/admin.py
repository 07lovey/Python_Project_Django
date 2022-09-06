import imp
from django.contrib import admin
from . models import BookNowForm, ContactForm, FoodCare, services,Blogs
# Register your models here.
admin.site.register(services)
admin.site.register(BookNowForm)
admin.site.register(ContactForm)
admin.site.register(Blogs)
admin.site.register(FoodCare)