import os
import uuid

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import *
from .models import*
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

#
# from ..Asus_laptop.settings import EMAIL_HOST_USER


def index(request):

    x=pmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    de=[]
    id=[]
    for i in x:
        a=i.pimage
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.pdescription
        de.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,de)

    return render(request,'index.html',{'mylist':mylist})

def contact(request):
    return render(request,'contact.html')
def usercontact(request,username):
    return render(request,'usercontact.html',{'username':username})

def contactus(request):

    a=ContactusForm()
    if request.method=='POST':
        sub=ContactusForm(request.POST)
        if sub.is_valid():
            em=sub.cleaned_data['mail']
            nm=sub.cleaned_data['Name']
            m=sub.cleaned_data['Email']
            ms=sub.cleaned_data['Message']



            send_mail(str(nm)+"||"+m+ "||"+"Enquaries",ms,EMAIL_HOST_USER,[em])
            return render(request,'success.html')
    return render(request,'contactus.html',{'form':a})

def about(request):
    return render(request,'about.html')

def userabout(request,username):
    return render(request,'userabout.html',{'username':username})

def adminreg(request):
    if request.method=='POST':
        a= adminregform(request.POST)
        if a.is_valid():
            fn = a.cleaned_data["fname"]
            ln = a.cleaned_data["lname"]
            un = a.cleaned_data["username"]
            dob=a.cleaned_data["dob"]
            em = a.cleaned_data["email"]
            pas = a.cleaned_data["password"]
            cpas=a.cleaned_data["cpassword"]
            if pas==cpas:
                b = adminregmodel(fname=fn, lname=ln, username=un,dob=dob, email=em, password=pas)
                b.save()
                return redirect(adminlog)
        else:
                return HttpResponse("registraion failed ")
    return render(request, 'adminreg.html')

def adminlog(request):
    if request.method=='POST':
        a=adminlogform(request.POST)
        if a.is_valid():
            un=a.cleaned_data["username"]
            request.session['username'] = un
            pas=a.cleaned_data["password"]
            b=adminregmodel.objects.all()
            for i in b:
                request.session['username']=i.username
                request.session['id'] = i.id
                if un==i.username and pas==i.password:
                    return redirect(f'/adminindex/{un}')
            else:

                return redirect(adminlog)
    return render(request,'admin log.html')

def adminindex(request,username):
    return render(request,'admin.html',{'username':username})

def profileedit(request,username):
    a=adminregmodel.objects.get(username=username)
    if request.method=='POST':
        a.fname=request.POST.get('fname')
        a.lname=request.POST.get('lname')
        a.username=request.POST.get('username')
        a.email=request.POST.get('email')
        a.password=request.POST.get('password')

        a.save()
        return redirect(f'/adminindex/{a.username}')
    return render(request,'profileedit.html',{'a':a,'username':username})

def productupload(request,username):

    if request.method=='POST':
        adminregmodel.objects.get(username=username)
        uid=request.session['id']

        a=pform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data["pname"]
            pr=a.cleaned_data["price"]
            de=a.cleaned_data["pdescription"]
            im=a.cleaned_data["pimage"]
            b=pmodel(uid=uid,pname=nm,price=pr,pdescription=de,pimage=im)
            b.save()
            return redirect(f'/adminindex/{username}')
        else:
            return HttpResponse("item adding failed")
    return render(request,'pupload.html',{'username':username})



# letest prodeuct

def pdisplay(request):

    id1 = request.session['id']
    y=request.session['username']

    x=pmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    de=[]
    id=[]
    uid=[]
    for i in x:
        u=i.uid
        uid.append(u)
        a=i.pimage
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.pdescription
        de.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,de,id,uid)

    return render(request,'pdisplay.html',{'mylist':mylist,'userid':id1,'username':y})

def pdelete(request,id):
    a=pmodel.objects.get(id=id)
    if len(a.pimage)>0:
        os.remove(a.pimage.path)
    a.delete()
    return redirect(pdisplay)

def pedit(request,id):
    a=pmodel.objects.get(id=id)
    im=str(a.pimage).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES)>0:
            if len(a.pimage)>0:
                os.remove(a.pimage.path)
            a.pimage=request.FILES['pimage']
        a.pname=request.POST.get('pname')
        a.price=request.POST.get('price')
        a.pdescription=request.POST.get('pdescription')
        a.save()
        return redirect(pdisplay)
    return render(request,'pedit.html',{'a':a,'im':im})

# zenbook

def zupload(request,username):

    if request.method=='POST':
        adminregmodel.objects.get(username=username)
        uid=request.session['id']

        a=zform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data["pname"]
            pr=a.cleaned_data["price"]
            de=a.cleaned_data["pdescription"]
            im=a.cleaned_data["pimage"]
            b=zmodel(uid=uid,pname=nm,price=pr,pdescription=de,pimage=im)
            b.save()
            return redirect(f'/adminindex/{username}')
        else:
            return HttpResponse("item adding failed")
    return render(request,'pupload.html',{'username':username})





def zdisplay(request):

    id1 = request.session['id']
    y=request.session['username']

    x=zmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    de=[]
    id=[]
    uid=[]
    for i in x:
        u=i.uid
        uid.append(u)
        a=i.pimage
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.pdescription
        de.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,de,id,uid)

    return render(request,'zendisplay.html',{'mylist':mylist,'userid':id1,'username':y})

def zdelete(request,id):
    a=zmodel.objects.get(id=id)
    if len(a.pimage)>0:
        os.remove(a.pimage.path)
    a.delete()
    return redirect(zdisplay)

def zedit(request,id):
    a=zmodel.objects.get(id=id)
    im=str(a.pimage).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES)>0:
            if len(a.pimage)>0:
                os.remove(a.pimage.path)
            a.pimage=request.FILES['pimage']
        a.pname=request.POST.get('pname')
        a.price=request.POST.get('price')
        a.pdescription=request.POST.get('pdescription')
        a.save()
        return redirect(zdisplay)
    return render(request,'pedit.html',{'a':a,'im':im})

# vivibook

def vupload(request,username):

    if request.method=='POST':
        adminregmodel.objects.get(username=username)
        uid=request.session['id']

        a=vform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data["pname"]
            pr=a.cleaned_data["price"]
            de=a.cleaned_data["pdescription"]
            im=a.cleaned_data["pimage"]
            b=vmodel(uid=uid,pname=nm,price=pr,pdescription=de,pimage=im)
            b.save()
            return redirect(f'/adminindex/{username}')
        else:
            return HttpResponse("item adding failed")
    return render(request,'pupload.html',{'username':username})





def vdisplay(request):

    id1 = request.session['id']
    y=request.session['username']

    x=vmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    de=[]
    id=[]
    uid=[]
    for i in x:
        u=i.uid
        uid.append(u)
        a=i.pimage
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.pdescription
        de.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,de,id,uid)

    return render(request,'vivodisplay.html',{'mylist':mylist,'userid':id1,'username':y})

def vdelete(request,id):
    a=vmodel.objects.get(id=id)
    if len(a.pimage)>0:
        os.remove(a.pimage.path)
    a.delete()
    return redirect(vdisplay)

def vedit(request,id):
    a=vmodel.objects.get(id=id)
    im=str(a.pimage).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES)>0:
            if len(a.pimage)>0:
                os.remove(a.pimage.path)
            a.pimage=request.FILES['pimage']
        a.pname=request.POST.get('pname')
        a.price=request.POST.get('price')
        a.pdescription=request.POST.get('pdescription')
        a.save()
        return redirect(vdisplay)
    return render(request,'pedit.html',{'a':a,'im':im})

# rog
def rupload(request,username):

    if request.method=='POST':
        adminregmodel.objects.get(username=username)
        uid=request.session['id']

        a=rform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data["pname"]
            pr=a.cleaned_data["price"]
            de=a.cleaned_data["pdescription"]
            im=a.cleaned_data["pimage"]
            b=rmodel(uid=uid,pname=nm,price=pr,pdescription=de,pimage=im)
            b.save()
            return redirect(f'/adminindex/{username}')
        else:
            return HttpResponse("item adding failed")
    return render(request,'pupload.html',{'username':username})




def rdisplay(request):

    id1 = request.session['id']
    y=request.session['username']

    x=rmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    de=[]
    id=[]
    uid=[]
    for i in x:
        u=i.uid
        uid.append(u)
        a=i.pimage
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.pdescription
        de.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,de,id,uid)

    return render(request,'rogdisplay.html',{'mylist':mylist,'userid':id1,'username':y})

def rdelete(request,id):
    a=rmodel.objects.get(id=id)
    if len(a.pimage)>0:
        os.remove(a.pimage.path)
    a.delete()
    return redirect(rdisplay)

def redit(request,id):
    a=rmodel.objects.get(id=id)
    im=str(a.pimage).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES)>0:
            if len(a.pimage)>0:
                os.remove(a.pimage.path)
            a.pimage=request.FILES['pimage']
        a.pname=request.POST.get('pname')
        a.price=request.POST.get('price')
        a.pdescription=request.POST.get('pdescription')
        a.save()
        return redirect(rdisplay)
    return render(request,'pedit.html',{'a':a,'im':im})

# tuf

def tupload(request,username):

    if request.method=='POST':
        adminregmodel.objects.get(username=username)
        uid=request.session['id']

        a=tform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data["pname"]
            pr=a.cleaned_data["price"]
            de=a.cleaned_data["pdescription"]
            im=a.cleaned_data["pimage"]
            b=tmodel(uid=uid,pname=nm,price=pr,pdescription=de,pimage=im)
            b.save()
            return redirect(f'/adminindex/{username}')
        else:
            return HttpResponse("item adding failed")
    return render(request,'pupload.html',{'username':username})





def tdisplay(request):

    id1 = request.session['id']
    y=request.session['username']

    x=tmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    de=[]
    id=[]
    uid=[]
    for i in x:
        u=i.uid
        uid.append(u)
        a=i.pimage
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.pdescription
        de.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,de,id,uid)

    return render(request,'tufdisplay.html',{'mylist':mylist,'userid':id1,'username':y})

def tdelete(request,id):
    a=tmodel.objects.get(id=id)
    if len(a.pimage)>0:
        os.remove(a.pimage.path)
    a.delete()
    return redirect(tdisplay)

def tedit(request,id):
    a=tmodel.objects.get(id=id)
    im=str(a.pimage).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES)>0:
            if len(a.pimage)>0:
                os.remove(a.pimage.path)
            a.pimage=request.FILES['pimage']
        a.pname=request.POST.get('pname')
        a.price=request.POST.get('price')
        a.pdescription=request.POST.get('pdescription')
        a.save()
        return redirect(tdisplay)
    return render(request,'pedit.html',{'a':a,'im':im})








def userreg(request):
    if request.method=='POST':
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        username=request.POST.get("username")
        email= request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        if User.objects.filter(username=username).first():
            messages.success(request,'Username already taken')
            return redirect(userreg)

        if User.objects.filter(email=email).first():
            messages.success(request,'Email already exist')
            return redirect(userreg)

        user_obj=User(first_name=fname,last_name=lname,username=username,email=email)
        if password==cpassword:
            user_obj.set_password(password)
            user_obj.save()
        auth_token=str(uuid.uuid4())
        profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email,auth_token)
        return render(request,'success.html')
    return render(request,'userreg.html')

def send_mail_regis(email,auth_token):
    subject="your account has been verified"
    message=f'paste the link verify your account http://127.0.0.1:8000/verify/{auth_token}'
    email_form=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_form,recipient)

def verify(request,auth_token):
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account is already verified')
            return redirect(userlogin)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(userlogin)
    else:
        messages.success(request,"user.html not found")
        return redirect(userlogin)

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        request.session['username']=username
        password=request.POST.get('password')





        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:   #if user.html doesn't exist
            messages.success(request,'User not found')
            return redirect(userlogin)

        profile_obj=profile.objects.filter(user=user_obj).first()
        a=profile.objects.all()
        for i in a:
            id=i.id
            request.session['id']=id
            email=i.user.email
            request.session['email']=email
        if not profile_obj.is_verified:
            messages.success(request,'profile not verified check your mail')
            return redirect(userlogin)
        user=authenticate(username=username,password=password)


        if user is None:
            messages.success(request,'wrong password or Email')
            return redirect(userlogin)
        return redirect(f'/userindex/{username}')
    return render(request,'userlogin.html')

def userindex(request,username):


    x=pmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    de=[]
    id=[]
    for i in x:
        a=i.pimage
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.pdescription
        de.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,de,id)

    return render(request,'userindex.html',{'mylist':mylist,"username":username})

def zen(request,username):
    x=zmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    de=[]
    id=[]
    uid=[]
    for i in x:
        u=i.uid
        uid.append(u)
        a=i.pimage
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.pdescription
        de.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,de,id,uid)

    return render(request,'zen.html',{'mylist':mylist,'username':username})

def vivo(request,username):

    x=vmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    de=[]
    id=[]
    uid=[]
    for i in x:
        u=i.uid
        uid.append(u)
        a=i.pimage
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.pdescription
        de.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,de,id,uid)

    return render(request,'vivo.html',{'mylist':mylist,'username':username})

def rog(request,username):

    x=rmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    de=[]
    id=[]
    uid=[]
    for i in x:
        u=i.uid
        uid.append(u)
        a=i.pimage
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.pdescription
        de.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,de,id,uid)

    return render(request,'rog.html',{'mylist':mylist,'username':username})

def tuf(request,username):
    x=tmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    de=[]
    id=[]
    uid=[]
    for i in x:
        u=i.uid
        uid.append(u)
        a=i.pimage
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.pdescription
        de.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,de,id,uid)

    return render(request,'tuf.html',{'mylist':mylist,'username':username})

def userprofile(request,username):
    x=mymodel.objects.all()
    nm=[]
    mid=[]
    da=[]
    id=[]
    # uid=[]
    for i in x:
        # u=i.uid
        # uid.append(u)
        b=i.myname
        nm.append(b)
        c=i.myid
        mid.append(c)
        d=i.mydate
        da.append(d)
        e=i.id
        id.append(e)
    mylist=zip(nm,mid,da,id)
    return render(request, 'userprofile.html',{'mylist':mylist,"username":username})

def mydelete(request,username,id):
    a=mymodel.objects.get(id=id)
    a.delete()
    return redirect(f'/userprofile/{username}')

def myproduct(request,username):

    if request.method=='POST':
        # uid=request.session['id']

        a=myform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data["myname"]
            id=a.cleaned_data["myid"]
            da=a.cleaned_data["mydate"]
            b=mymodel(myname=nm,myid=id,mydate=da)
            b.save()
            return redirect(f'/userprofile/{username}')
        else:
            return HttpResponse("item adding failed")
    return render(request,'add product.html',{'username':username})

def useredit(request,username):
    a=User.objects.get(username=username)
    if request.method=='POST':
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.username=request.POST.get('username')
        a.email=request.POST.get('email')
        a.password=request.POST.get('password')
        a.save()
        return redirect(f'/userindex/{a.username}')
    return render(request,'useredit.html',{'a':a,'username':username})

def pcart(request,id):
    a=pmodel.objects.get(id=id)
    uid=request.session['id']
    b=cartmodel(uid=uid,cartimage=a.pimage,cartname=a.pname,cartprice=a.price,cartdescription=a.pdescription)
    b.save()
    return render(request,'cartsuccess.html')

def zcart(request,id):
    a=zmodel.objects.get(id=id)
    uid=request.session['id']
    b=cartmodel(uid=uid,cartimage=a.pimage,cartname=a.pname,cartprice=a.price,cartdescription=a.pdescription)
    b.save()
    return render(request,'cartsuccess.html')

def vcart(request,id):
    a=vmodel.objects.get(id=id)
    uid=request.session['id']
    b=cartmodel(uid=uid,cartimage=a.pimage,cartname=a.pname,cartprice=a.price,cartdescription=a.pdescription)
    b.save()
    return render(request,'cartsuccess.html')

def rcart(request,id):
    a=rmodel.objects.get(id=id)
    uid=request.session['id']
    b=cartmodel(uid=uid,cartimage=a.pimage,cartname=a.pname,cartprice=a.price,cartdescription=a.pdescription)
    b.save()
    return render(request,'cartsuccess.html')

def tcart(request,id):
    a=tmodel.objects.get(id=id)
    uid=request.session['id']
    b=cartmodel(uid=uid,cartimage=a.pimage,cartname=a.pname,cartprice=a.price,cartdescription=a.pdescription)
    b.save()
    return render(request,'cartsuccess.html')

def cartdisplay(request,username):

    id1=request.session['id']
    x=cartmodel.objects.all()
    image = []
    name = []
    price = []
    des = []
    id = []
    uid=[]
    for i in x:
        u = i.uid
        uid.append(u)
        a = i.cartimage
        image.append(str(a).split('/')[-1])
        b = i.cartname
        name.append(b)
        c = i.cartprice
        price.append(c)
        d = i.cartdescription
        des.append(d)
        e = i.id
        id.append(e)
    mylist = zip(image, name, price, des, id,uid)

    return render(request,'cartdisplay.html',{'mylist':mylist,'userid':id1,'username':username})


def cartdelete(request,username,id):
    a=cartmodel.objects.get(id=id)
    a.delete()
    return redirect(f'/cartdisplay/{username}')

def buy(request,username,id):
    a=cartmodel.objects.get(id=id)
    if request.method=='POST':
        cartname=request.POST.get("name")
        cartprice = request.POST.get("price")
        cartquantity = request.POST.get("quantity")
        total=int(cartprice)*int(cartquantity)

        em=request.session['email']
        send_mail(str() + "||" + "Final bill", "ordered success ", EMAIL_HOST_USER, [em])
        return render(request,'bill.html',{'n':cartname,'p':cartprice,'q':cartquantity,'t':total,'username':username})

    return render(request,'buy.html',{'a':a,'username':username})




