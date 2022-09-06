
from rest_framework import serializers
from . models import Blogs, FoodCare, services,ContactForm,BookNowForm


class servicesSerializers(serializers.ModelSerializer):   
        class Meta:
            model=services
            fields=('title','brief_Desc','details') 
            

class BlogsSerializers(serializers.ModelSerializer):   
        class Meta:
            model=Blogs
            fields=('card_title','card_text','card_link')  

class FoodCareSerializers(serializers.ModelSerializer):   
        class Meta:
            model=FoodCare
            fields=('card_title','card_text','card_link')  

class ContactForm(serializers.ModelSerializer):   
        class Meta:
            model=ContactForm
            fields=('firstname','lastname','emaildid','phoneno','address')  
        def clean(self):
            super(ContactForm, self).clean()

      # getting username and password from cleaned_data
            firstname = self.cleaned_data.get('firstname')
            lastname= self.cleaned_data.get('lastname')
            phoneno=self.cleaned_data.get('phoneno')
            address=self.cleaned_data.get('address')
            if len(firstname) < 10:
                 self._errors['firstname'] = self.error_class(['firstname should be of minimum 10 characters'])
            if len(lastname) < 10:
                self._errors['lastname'] = self.error_class(['lastname should be of minimum 10 characters'])
            if phoneno!=10:
                self._errors['lastname'] = self.error_class(['Invalid phone number'])
            return self.cleaned_data


class BookNowForm(serializers.ModelSerializer):   
        class Meta:
            model=BookNowForm
            fields=('firstname','lastname','emaildid','phoneno','address')  
        def clean(self):
            super(ContactForm, self).clean()

      # getting username and password from cleaned_data
            firstname = self.cleaned_data.get('firstname')
            lastname= self.cleaned_data.get('lastname')
            phoneno=self.cleaned_data.get('phoneno')
            address=self.cleaned_data.get('address')
            if len(firstname) < 10:
                 self._errors['firstname'] = self.error_class(['firstname should be of minimum 10 characters'])
            if len(lastname) < 10:
                self._errors['lastname'] = self.error_class(['lastname should be of minimum 10 characters'])
            if phoneno!=10:
                self._errors['lastname'] = self.error_class(['Invalid phone number'])
            return self.cleaned_data