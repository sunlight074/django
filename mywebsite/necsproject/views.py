from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


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
    return render(request, 'jobalert.html')

def maintable(request):
    return render(request ,"table.html")

def kanban(request):
    return render(request ,"kanban.html")

def dashboard(request):
    return render(request ,"dashboard.html")