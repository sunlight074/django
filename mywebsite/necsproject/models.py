from django.db import models
from django.contrib.auth.models import User

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
    owner = models.CharField(max_length=200, null=True)
    result = models.TextField(null=True)

    def __str__(self):
        return str(self.id)




# python manage.py makemigrations
# python manage.py migrate