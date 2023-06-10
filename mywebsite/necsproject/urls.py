from django.urls import path
from .views import *

urlpatterns = [
   # path('', login, name='login-page'),
    path('jobalert/', jobalert, name='jobalert-page'),  
    path('maintable/', maintable, name='maintable-page'),
    path('kanban/', kanban, name='kanban-page'),
    path('dashboard/', dashboard, name='dashboard-page'),

]
