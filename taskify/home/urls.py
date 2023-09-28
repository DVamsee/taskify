from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('filter/',views.filter,name='tasks filter'),
    path('filter/calender/<int:day>/<int:month>/<int:year>/',views.calender_tasks,name='filter_date'),
   
]