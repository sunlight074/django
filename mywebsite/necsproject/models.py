from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class job(models.Model):
    ID = models.AutoField(primary_key=True)
    _time = models.DateTimeField()
    namealert = models.CharField(max_length=200, null=True)
    severity = (
                ('L','Low'), 
                ('M','Medium'), 
                ('H','High'), 
                ('C','Critical'))
    priority = models.CharField(max_length=200, choices=severity)
    app = models.CharField(max_length=200, null=True)
    owner = models.CharField(max_length=200, null=True)
    result = models.TextField(null=True)

    def __str__(self):
        return self.namealert





# python manage.py makemigrations
# python manage.py migrate