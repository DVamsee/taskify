from django.urls import path
from . import  views

urlpatterns = [
    path('priority/<int:id>/<str:priority>/',views.priority_change, name='change priority'),
    path('status/<int:id>/<str:status>/',views.status_change, name='change status'),
    path('delete/<int:id>/',views.delete_task, name='delete task'),
    path('add/task/',views.add_task, name='add task'),
    
]