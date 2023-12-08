from django.shortcuts import render, redirect
from django import forms
from .models import members


all_members = members.objects.all

def gym(request):
    
    if request.method == 'POST':
        
        name = request.POST('name')
        email = request.POST('email')
        phone = request.POST('phone')
        city = request.POST('city')
        print("respose submitted")
    else:
        return render(request, 'gym.html')


def sum(request):
    return render(request, 'submit.html')

def show(request):
    return render(request , 'showdata.html', {'all' : all_members})
