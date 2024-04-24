from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from.models import *
from.forms import *
#involving decorators to implement authentication
#a decorator is a function that adds functionality to an existing function
from django.contrib.auth.decorators import login_required

# Create your views here.

# def osman(request):
#     return render(request, 'kesho_app/kesho.html')
def index(request):
    return render(request, 'kesho_app/index.html')
def home(request):
    return render(request, 'kesho_app/home.html')
@login_required
def about(request):
    return render(request, 'kesho_app/about.html')
def jumper(request):
    return render(request, 'kesho_app/jumper.html')
def babe(request):
    return render(request, 'kesho_app/babe.html')

#trying to add a babe form
#pk is anything or any word...a representation of primary key, a unique id
def Add_babe(request):
    getbabeform = Addbabe()
    return render(request, 'kesho_app/babe.html', {'getbabeform': getbabeform,})


#Addedbabe = Baby.objects.get(id=PK)getting all instances of registered babes
 # babesForm = Addbabe(request.POST)
    
    # if request.method == 'POST':
    #     if babesForm.is_valid():
    #         newbabe = babesForm.save(commit=False)
    #         newbabe.save
    
def Addpayment(request):
    getpaymentform = AddpaymentForm()
    return render(request, 'kesho_app/payment.html', {'getpaymentform': getpaymentform,})
