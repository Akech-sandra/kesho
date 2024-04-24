from django.urls import path
from kesho_app import views
#accessing the functionality of login view inbuilt in django to correspond to line 14
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("kesho", views.osman, name = 'kesho'),
    path("", views.index, name = 'index'),
    path("home/", views.home, name = 'home'),
    path("about/", views.about, name = 'about'),
    path("babe/", views.Add_babe, name = 'Add_babe'),
    path("jumper/", views.jumper, name = 'jumper'),
    path("payment/", views.Addpayment, name = 'Addpayment'),
    path('login/', auth_views.LoginView.as_view(template_name = 'kesho_app/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'kesho_app/logout.html'), name = 'logout'),
    
    ]#urls must be connected to views. urls require a view to respond to it. a view is a function
    #blank requests represents an index page
    #urls is a request
    #tables are models
    #the columns of a table are the attributes of the of a class...frame work of a table is a class
    
    
    #bcoz both the browser and the codes are on my computer..it is a local host 127.0.1:8000 '8000'-is a connecting port btn the browser and the server