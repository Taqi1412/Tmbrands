from django.shortcuts import render,HttpResponse
from datetime import datetime
from Tmapps.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
  #  return HttpResponse("THIS IS HOME PAGE")
def Home(request):
    return render(request,'index.html')
   
def About(request):
    return render(request,'About.html')

def Contact(request):
   if request.method == "POST" :
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone =request.POST.get('phone')
    desc =request.POST.get('desc')
  #  contact=Contact(name=name,email=email,phone=phone,desc=desc, datetime=datetime.today())
    Contact.save(name=name,email=email,phone=phone,desc=desc, datetime=datetime.today())
   return render(request,'Contact.html')
def ShopNewCars(request):
    return render(request,'newcars.html')

def ClearenceEvent(request):
        return render(request,'event.html')

def OwnedShop(request):
        return render(request,'owned.html')       

def JEANSANDSHIRTS(request):
        return HttpResponse("JENS AND SHIRTS ARE NOT AVAILABLE")

def MOBILE(request):
        return render(request,'mobiles.html')

def services(request):
        return render(request,'services.html')
def myModal(request):
        return render (request,"myModal.html")

def LAPTOP(request):      
        return render(request,'laptop.html')


