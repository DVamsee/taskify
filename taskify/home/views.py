from django.shortcuts import render

# Create your views here.

def homepage(request, *args, **kwargs):
    return render(request,'home.html')