from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Task,Collaborator, Comment
import datetime

from .forms import AddTask

# Create your views here.

User = get_user_model()

@login_required
def add_task(request, *args,**kwargs):
    if request.method =='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        print(request.POST)
        if title == '':

            messages.info(request,'Enter Title')
            return render(request,'task.html')
        if due_date == '':
            due_date = datetime.datetime.now()
        user = request.user
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()
        obj = Task.objects.create(title=title, description= description, priority= priority,status = status, due_date=due_date,user_id= user, created_at=created_at,updated_at=updated_at)
        obj.save()

        return redirect('/')
    return render(request,'task.html')

        

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
        task.delete()
        return redirect('/')
    

@login_required
def add_comment(request,task, *args, **kwargs):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        task = Task.objects.get(id=task)
        if task:
            time = datetime.datetime.now()
            comment = Comment.objects.create(task_id = task,user_id = request.user,text=comment,created_at = time)
            comment.save()
            return redirect('/')
        
@login_required
def delete_comment(request,comment, *args, **kwargs):
    comment = Comment.objects.get(id = comment)
    if comment:
        comment.delete()
        return redirect('/')
