from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .models import *
from django.http import JsonResponse

def updateDescription(request):
    ticket = jobAlert.objects.get(id=request.GET.get('jobPk',None))
    ticket_object = ticket[0] if isinstance(ticket, tuple) else ticket
    ticket_object.description = request.GET.get('description',None)
    ticket_object.save()
    
    return JsonResponse(data="success",safe=False) 

def updateStatus(request):
    ticket = jobAlert.objects.get(id=request.GET.get('jobPk',None))
    ticket_object = ticket[0] if isinstance(ticket, tuple) else ticket
    ticket_object.status = request.GET.get('status',None)
    ticket_object.save()
    
    return JsonResponse(data="success",safe=False)

def getMainTableData(request):
    jobData = jobAlert.objects.all() #เป็นฟังก์ชันสำหรับการดึงข้อมูล
    data_json = serializers.serialize('json', jobData) #แปลงข้อมูลให้เป็น json
    return JsonResponse(data_json,safe=False) #return คือการส่งข้อมูลกลับ

def updateJobalertById(request):
    ticket = jobAlert.objects.get(id=request.GET.get('jobPk',None))
    ticket_object = ticket[0] if isinstance(ticket, tuple) else ticket
    ticket_object.assign = User.objects.get(id=request.GET.get('assignee_value',None))
    ticket_object.report = User.objects.get(id=request.GET.get('reporter_value',None)) 
    ticket_object.app = request.GET.get('app_value',None)

    ticket_object.save()

    return JsonResponse(data="success",safe=False)

def getJobalertById(request):
    ticket_id = request.GET.get('ticket_id', None) 
    data = jobAlert.objects.filter(ticket_id__icontains=ticket_id)
    data_json = serializers.serialize('json', data)
    return JsonResponse(data_json,safe=False)

def getUserInfo(request):
    id = request.GET.get('id', None)
    userInfo = User.objects.filter(pk=id)
    data_json = serializers.serialize('json', userInfo)
    return JsonResponse(data_json,safe=False)

def getJobalertData(request):
    severity = request.GET.get('severity', None) 
    person = request.GET.get('person', None)
    search = request.GET.get('search', None)

    if severity and person and search:
        data = jobAlert.objects.filter(severity=severity ,assign=person ,search_name__icontains=search)
        data_json = serializers.serialize('json', data)
        return JsonResponse(data_json,safe=False)
    elif severity and person :
        data = jobAlert.objects.filter(severity=severity ,assign=person)
        data_json = serializers.serialize('json', data)
        return JsonResponse(data_json,safe=False)
    elif severity and search :
        data = jobAlert.objects.filter(severity=severity ,search_name__icontains=search)
        data_json = serializers.serialize('json', data)
        return JsonResponse(data_json,safe=False)
    elif person and search :
        data = jobAlert.objects.filter(assign=person ,search_name__icontains=search)
        data_json = serializers.serialize('json', data)
        return JsonResponse(data_json,safe=False)
    elif severity:
        data = jobAlert.objects.filter(severity=severity)
        data_json = serializers.serialize('json', data)
        return JsonResponse(data_json,safe=False)
    elif person:
        data = jobAlert.objects.filter(assign=person)
        data_json = serializers.serialize('json', data)
        return JsonResponse(data_json,safe=False)
    elif search:
        data = jobAlert.objects.filter(search_name__icontains=search)
        data_json = serializers.serialize('json', data)
        return JsonResponse(data_json,safe=False)
    else:
        data = jobAlert.objects.all()
        data_json = serializers.serialize('json', data)
        return JsonResponse(data_json,safe=False)
    
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
    if request.POST.get('ticketId',False):
        print('assignee = ',request.POST.get('assignee',False))
        print('reporter = ',request.POST.get('reporter',False))
        print('app = ',request.POST.get('app',False))
        print('ticketId = ',request.POST.get('ticketId',False))
        

        ticket = jobAlert.objects.get(id=request.POST.get('ticketId',False))
        ticket_object = ticket[0] if isinstance(ticket, tuple) else ticket

        ticket_object.assign = User.objects.get(id=request.POST.get('assignee',False))
        ticket_object.report = User.objects.get(id=request.POST.get('reporter',False)) 
        ticket_object.app = request.POST.get('app',False)

        ticket_object.save()

    return render(request, 'jobalert.html')

def maintable(request):
    # if 'edit' in request.POST:
    #     ticket = MANAGE_TICKET.objects.get(ticket_id=request.POST['edit'])
    #     ticket_object = ticket[0] if isinstance(ticket, tuple) else ticket
    #     ticket_object.status = request.POST['edit_status']
    #     ticket_object.save()
    # elif 'create' in request.POST:
    #     job = request.POST['job']
    #     category = request.POST['category']
    #     severity = request.POST['severity']
    #     assignee = request.POST['assignee']
    #     #type = request.POST['type']
    #     reporter = request.POST['reporter']
    #     description = request.POST.get('description',False)
        
    #     obj = MANAGE_TICKET(
    #         job_id=Job.objects.get(id= job),
    #         category_attack=category,
    #         severity=severity,
    #         assignee=assignee,
    #         #type=type,
    #         reporter=reporter,
    #         description=description)
        
    #     obj.save()

    # jobData = Job.objects.all().values()
    # ticket = MANAGE_TICKET.objects.all().values()
    # jobData = jobAlertDetail.objects.select_related('alert_detail_assign')
    return render(request ,"table.html" , context={'data' : 'jobData' , 'ticket':""})

def kanban(request):
    return render(request ,"kanban.html")

def jobDetails(request , id):
    return render(request , "jobdetails.html")

def details(request, id):
    # jobData = Job.objects.get(id= id)
    # data = json.loads(jobData.result)

    # sid = data["sid"]
    # searchName = data['search_name']
    # app = data['app']
    # owner = data['owner']
    # resultsLink = data['results_link']
    # result = data['result']

    # context = {
    #     'sid':sid ,
    #     'searchName':searchName ,
    #     'app':app ,
    #     'owner':owner ,
    #     'resultsLink':resultsLink ,
    #     'result':result ,
    # }
    return render(request ,"details.html")

def dashboard(request):
    return render(request ,"dashboard.html")