from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('filter/',views.filter,name='tasks filter'),
    path('add/task/',views.add_task,name='add task'),
]