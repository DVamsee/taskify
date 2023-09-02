from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='registration'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('edit/',views.edit_profile,name='edit profile'),
    
]