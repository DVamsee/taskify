from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Task,Collaborator, Comment

# Create your views here.

User = get_user_model()

@login_required
def add_task(request, *args,**kwargs):
    pass

@login_required
def priority_change(request,id,priority, *args, **kwargs):
    task = Task.objects.get(id = id)
    if request.user.is_authenticated and task:
        task.priority = priority
        task.save(update_fields=['priority'])
        return redirect('/')
    return redirect('/')

@login_required
def status_change(request,id,status, *args, **kwargs):
    task = Task.objects.get(id = id)
    if request.user.is_authenticated and task:
        task.status = status
        task.save(update_fields=['status'])
        return redirect('/')
    return redirect('/')