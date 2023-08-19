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
    path('ajax/getJobAlert/',  getJobalertData, name='get-job-alert'),
    path('ajax/getUserInfo/',  getUserInfo, name='get-user-info'),
    path('ajax/getJobalertById/', getJobalertById, name='get-job-alert-id'),
    path('ajax/updateJobalertById/', updateJobalertById, name='update-job-alert-id'),
    path('ajax/updateStatus/', updateStatus, name='update-status'),
    path('ajax/updateDescription/', updateDescription, name='update-description'),
    path('ajax/getMaintable/', getMainTableData, name='get-main-table-data'),
]