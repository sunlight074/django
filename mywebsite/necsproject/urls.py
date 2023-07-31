from django.urls import path
from .views import *

urlpatterns = [
   # path('', login, name='login-page'),
    path('jobalert/', jobalert, name='jobalert-page'),  
    path('maintable/', maintable, name='maintable-page'),
    path('kanban/', kanban, name='kanban-page'),
    path('details/<int:id>', details, name='details-page'),
    path('job-details/<int:id>', jobDetails, name='job-details-page'),
    path('dashboard/', dashboard, name='dashboard-page'),
]