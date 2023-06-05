from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request ,"login.html")

def jobAlert(request):
    return render(request ,"jobAlert.html")

def mainTable(request):
    return render(request ,"table.html")

def kanban(request):
    return render(request ,"kanban.html")

def dashboard(request):
    return render(request ,"dashboard.html")