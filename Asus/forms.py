from django import forms
from django.contrib.auth.models import User
from .models import *


class adminregform(forms.Form):
    fname = forms.CharField(max_length=15)
    lname = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    dob = forms.DateField()
    email = forms.EmailField()
    password = forms.CharField(max_length=50)
    cpassword = forms.CharField(max_length=50)


class adminlogform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=50)

class ContactusForm(forms.Form):
    mail=forms.EmailField()
    Name=forms.CharField(max_length=30)
    Email=forms.EmailField()
    Message=forms.CharField(max_length=1000,
                            widget=forms.Textarea(attrs={'rows':5,'cols':50}))


class pform(forms.Form):
    pname = forms.CharField(max_length=500)
    price = forms.IntegerField()
    pdescription = forms.CharField(max_length=2500)
    pimage = forms.ImageField()

class zform(forms.Form):
    pname = forms.CharField(max_length=500)
    price = forms.IntegerField()
    pdescription = forms.CharField(max_length=2500)
    pimage = forms.ImageField()

class vform(forms.Form):
    pname = forms.CharField(max_length=500)
    price = forms.IntegerField()
    pdescription = forms.CharField(max_length=2500)
    pimage = forms.ImageField()

class rform(forms.Form):
    pname = forms.CharField(max_length=500)
    price = forms.IntegerField()
    pdescription = forms.CharField(max_length=2500)
    pimage = forms.ImageField()

class tform(forms.Form):
    pname = forms.CharField(max_length=500)
    price = forms.IntegerField()
    pdescription = forms.CharField(max_length=2500)
    pimage = forms.ImageField()

class myform(forms.Form):
    # uid=forms.IntegerField()
    myname=forms.CharField(max_length=500)
    myid=forms.IntegerField()
    mydate=forms.DateField()
    def __str__(self):
        return self.myname
