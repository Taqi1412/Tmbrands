from django.contrib import admin
from django.urls import path
from Tmapps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index, name='home'),
     path("Home",views.Home, name='Home'),
    path("About",views.About, name='About'),
    path("Contact",views.Contact, name='Contact'),
    path("ShopNewCars",views.ShopNewCars, name='ShopNewCars'),
    path("OwnedShop" ,views.OwnedShop,name= 'OwnedShop'),
    path("ClearenceEvent",views.ClearenceEvent, name='ClearenceEvent'),
    path("ShopNewCars",views.ShopNewCars, name='ShopNewCars'),
    path("Contact",views.Contact, name='Contact'),
    path("MOBILE",views.MOBILE, name='MOBILE'),
    path("LAPTOP",views.LAPTOP, name='LAPTOP'),
    path("myModal",views.myModal, name='myModal'),
    path("LAPTOP",views.LAPTOP, name='LAPTOP'),
    path("services",views.services, name='services'),
    path("Contact",views.Contact, name='Contact'),

]
