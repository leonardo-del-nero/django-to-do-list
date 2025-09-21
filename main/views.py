from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(respoonse, id):
    
    ls = ToDoList.objects.get(id=id)
    return render(respoonse, 'main/list.html', {"ls":ls})

def home(response):
    return render(response, 'main/home.html', {})



