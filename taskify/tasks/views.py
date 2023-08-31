from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Task,Collaborator, Comment

import datetime

# Create your views here.

User = get_user_model()

@login_required
def add_task(request, *args,**kwargs):
    if request.method =='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        due = request.POST.get('due')
        category = 'personal'
        user = request.user
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()
        if title == 'None':
            messages.info(request, 'Task title is required')
            return render(request, 'task.html',)


        return HttpResponse(f'{title} {description} {priority} {status} {due}   ')

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

@login_required
def delete_task(request,id, *args, **kwargs):
    task = Task.objects.get(id=id)
    if task:
        return HttpResponse(f'delete task:{task.title}')