from django.contrib.auth import authenticate ,login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from bitapp.models import bitmartdb,bitdb,prodb
from vegfoodapp.models import adcontact
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.
def index3(request):
    return render(request,"index3.html")
def adminpage(request):
    return render(request,"addadmin.html")
def savedata(request):
    if request.method=="POST":
        na=request.POST.get('name')
        img = request.FILES['image']
        em=request.POST.get('email')
        mo=request.POST.get('mob')
        ps=request.POST.get('pswd')
        cs=request.POST.get('cpswd')
        un=request.POST.get('uname')
        obj=bitmartdb(name=na,image=img,email=em,mob=mo,pswd=ps,cpswd=cs,uname=un)
        obj.save()
        return redirect(adminpage)
def adminpage2(request):
    data = bitmartdb.objects.all()
    return render(request, "viewadmin.html", {'data': data})

def editpage(request,dataid):
    data=bitmartdb.objects.get(id=dataid)
    print(data)
    return render(request,"adminedit.html",{'data':data})
def updatedata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mo = request.POST.get('mob')
        ps = request.POST.get('pswd')
        cs = request.POST.get('cpswd')
        un = request.POST.get('uname')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=bitmartdb.objects.get(id=dataid).image
        bitmartdb.objects.filter(id=dataid).update(name=na,image=file,email=em,mob=mo,pswd=ps,cpswd=cs,uname=un)
        return redirect(adminpage2)

def deletedata(request,dataid):
    data=bitmartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(adminpage2)
def categorypage(request):
    return render(request,"addcategory.html")
def savedataa(request):
    if request.method=="POST":
        na=request.POST.get('name')
        img = request.FILES['image']
        de=request.POST.get('desc')
        obj = bitdb(name=na, image=img,desc=de)
        obj.save()
        return redirect(categorypage)
def cate(request):
    data = bitdb.objects.all()
    return render(request, "viewcategory.html", {'data': data})

def editpage2(request,dataid):
    data=bitdb.objects.get(id=dataid)
    print(data)
    return render(request,"catedit.html",{'data':data})
def updatedataa(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=bitdb.objects.get(id=dataid).image
        bitdb.objects.filter(id=dataid).update(name=na,image=file,desc=de)
        return redirect(cate)

def deletedataa(request,dataid):
    data=bitdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cate)
def productpage(request):
    data = bitdb.objects.all()
    return render(request, "addproduct.html", {'data': data})

def savedata3(request):
    if request.method=="POST":
        cat=request.POST.get('cname')
        img = request.FILES['image']
        pna = request.POST.get('pname')
        pi = request.POST.get('price')
        qu = request.POST.get('qua')
        de = request.POST.get('desc')

        obj=prodb(image=img,desc=de,category=cat,pname=pna,pri=pi,qua=qu)
        obj.save()
        return redirect(productpage)
def product2(request):
    data = prodb.objects.all()
    return render(request, "viewproduct.html", {'data': data})

def editp(request,dataid):
    data=prodb.objects.get(id=dataid)
    da=bitdb.objects.all()
    print(data)
    return render(request,"proedit.html",{'data':data,'da':da})
def updatedatap(request,dataid):
    if request.method=="POST":
        cat = request.POST.get('cname')
        pna = request.POST.get('pname')
        pi = request.POST.get('price')
        qu = request.POST.get('qua')
        de = request.POST.get('desc')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=prodb.objects.get(id=dataid).image
        prodb.objects.filter(id=dataid).update(image=file,desc=de,category=cat,pname=pna,pri=pi,qua=qu)
        return redirect(product2)

def deletedatta(request,dataid):
    data=prodb.objects.filter(id=dataid)
    data.delete()
    return redirect(product2)

def loginpage(request):
    return render(request,"login.html")
def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")

        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(index3)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
def contact(request):
    data = adcontact.objects.all()
    return render(request,"message.html",{'data':data})