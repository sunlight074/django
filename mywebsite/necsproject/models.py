from django.db import models
from django.contrib.auth.models import User

class jobAlert(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    search_name = models.CharField(max_length=200, null=True)
    result_link = models.CharField(max_length=200, null=True)
    results = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class jobAlertDetail(models.Model):
    id = models.AutoField(primary_key=True)
    alert_detail_assign = models.ForeignKey(jobAlert, on_delete=models.CASCADE, related_name='alert_detail_assign')
    assign = models.OneToOneField(User, null=True, on_delete=models.CASCADE , related_name='assign')
    report = models.OneToOneField(User, null=True, on_delete=models.CASCADE , related_name='report')
    app = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    job_detail_id = models.ForeignKey('jobAlertDetail', on_delete=models.CASCADE, related_name='job_detail_id')
    comment_person = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='comment_person')
    comment_text = models.CharField(max_length=200, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment_id)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #type = (
    #    ('tier1','tier1')
    #    ,('tier2','tier2')
    #    ,('tier3','tier3')
    #)
    #role = models.CharField(max_length=200, null=True, choices=type) 
    def __str__(self):
        return self.user.username

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    nameAlert = models.CharField(max_length=200, null=True)
    severity = (
                ('Low','Low'), 
                ('Medium','Medium'), 
                ('High','High'), 
                ('Critical','Critical'))
    priority = models.CharField(max_length=200, choices=severity)
    app = models.CharField(max_length=200, null=True)
    owner = models.CharField(max_length=200, null=True) #  ref. auth
    result = models.TextField(null=True)

    def __str__(self):
        return str(self.id)

#สร้างตาราง MANAGE_TICKET
class MANAGE_TICKET (models.Model):
    ticket_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey('Job', on_delete=models.CASCADE,related_name='job_id')
    category_attack = models.CharField(max_length=36)
    severityData = (
                ('Low','Low'), 
                ('Medium','Medium'), 
                ('High','High'), 
                ('Critical','Critical'))
    severity = models.CharField(max_length=200, choices=severityData)
    assignee =  models.CharField(max_length=255)
    #typeData = (('Scheduled','Scheduled'),('Real-time','Real-time'))
    #type = models.CharField(max_length=200, choices=typeData)
    reporter = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    description = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ticket_id)


# python manage.py makemigrations
# python manage.py migrate