from django.urls import path
from . import  views

urlpatterns = [
    path('priority/<int:id>/<str:priority>/',views.priority_change, name='change priority'),
    path('status/<int:id>/<str:status>/',views.status_change, name='change status'),
    
]