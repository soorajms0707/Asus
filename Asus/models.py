from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class adminregmodel(models.Model):
    fname=models.CharField(max_length=15)
    lname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    dob = models.DateField()
    email=models.EmailField()
    password=models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class pmodel(models.Model):
    uid=models.IntegerField()
    pname=models.CharField(max_length=500)
    price=models.IntegerField()
    pdescription=models.CharField(max_length=2500)
    pimage=models.ImageField(upload_to="Asus/static")
    def __str__(self):
        return self.pname

class zmodel(models.Model):
    uid=models.IntegerField()
    pname=models.CharField(max_length=500)
    price=models.IntegerField()
    pdescription=models.CharField(max_length=2500)
    pimage=models.ImageField(upload_to="Asus/static")
    def __str__(self):
        return self.pname

class vmodel(models.Model):
    uid=models.IntegerField()
    pname=models.CharField(max_length=500)
    price=models.IntegerField()
    pdescription=models.CharField(max_length=2500)
    pimage=models.ImageField(upload_to="Asus/static")
    def __str__(self):
        return self.pname

class rmodel(models.Model):
    uid=models.IntegerField()
    pname=models.CharField(max_length=500)
    price=models.IntegerField()
    pdescription=models.CharField(max_length=2500)
    pimage=models.ImageField(upload_to="Asus/static")
    def __str__(self):
        return self.pname

class tmodel(models.Model):
    uid=models.IntegerField()
    pname=models.CharField(max_length=500)
    price=models.IntegerField()
    pdescription=models.CharField(max_length=2500)
    pimage=models.ImageField(upload_to="Asus/static")
    def __str__(self):
        return self.pname

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

class mymodel(models.Model):
    # uid=models.IntegerField()
    myname=models.CharField(max_length=500)
    myid=models.IntegerField()
    mydate=models.DateField()
    def __str__(self):
        return self.myname

class cartmodel(models.Model):
    uid = models.IntegerField()
    cartname=models.CharField(max_length=20)
    cartprice=models.IntegerField()
    cartdescription=models.CharField(max_length=50)
    cartimage=models.ImageField(upload_to="Asus/static/cart")
    def __str__(self):
        return self.cartname

