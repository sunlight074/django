from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *



def login(request):

    if request.method == 'POST':
        return render(request ,"dashboard.html")
        # data = request.POST.copy()
        # username = data.get('username')
        # password = data.get('password')
        # print(username, password)
        # try:
        #     user = authenticate(username=username, password=password)
        #     login(request, user)
        # except:
        #     return HttpResponse('Invalid Login') 
        
    return render(request, 'login.html')

def jobalert(request):
    result = [
        {'id':1},
        {'id':2},
        {'id':3},
        {'id':4},
        {'id':5},
        {'id':6},
        {'id':7}
    ]
    return render(request, 'jobalert.html' , context={'data' : result })

def maintable(request):
    return render(request ,"table.html")

def kanban(request):
    return render(request ,"kanban.html")

def details(request, id):
    return render(request ,"details.html", context={'id':id})

def dashboard(request):
    return render(request ,"dashboard.html")