from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
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
    owner = models.CharField(max_length=200, null=True)
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
    reporter = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    description = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ticket_id)




# python manage.py makemigrations
# python manage.py migrate