from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *
import json



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
    if request.method == 'POST':
        deleteID = request.POST['delete']
        Job.objects.filter(id=deleteID).delete()
        
    jobData = Job.objects.all().values()

    return render(request, 'jobalert.html' , context={'data' : jobData })

def maintable(request):
    return render(request ,"table.html")

def kanban(request):
    return render(request ,"kanban.html")

def details(request, id):
    jobData = Job.objects.get(id= id)
    data = json.loads(jobData.result)

    sid = data["sid"]
    searchName = data['search_name']
    app = data['app']
    owner = data['owner']
    resultsLink = data['results_link']
    result = data['result']

    context = {
        'sid':sid ,
        'searchName':searchName ,
        'app':app ,
        'owner':owner ,
        'resultsLink':resultsLink ,
        'result':result ,
    }
    return render(request ,"details.html", context)

def dashboard(request):
    return render(request ,"dashboard.html")