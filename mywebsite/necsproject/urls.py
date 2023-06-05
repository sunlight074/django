from django.urls import path
from .views import login ,jobAlert

urlpatterns = [
    path('', login),
    path('job-alert', jobAlert),
]
