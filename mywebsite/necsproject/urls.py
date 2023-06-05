from django.urls import path
from .views import login ,jobAlert ,dashboard ,kanban ,mainTable

urlpatterns = [
    path('', login),
    path('job-alert', jobAlert),
    path('dashboard', dashboard),
    path('kanban', kanban),
    path('main-table', mainTable),
]
