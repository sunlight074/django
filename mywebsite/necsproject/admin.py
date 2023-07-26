from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(MANAGE_TICKET)
admin.site.register(jobAlert)
admin.site.register(jobAlertDetail)
admin.site.register(comment)