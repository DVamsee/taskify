from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import get_user_model
from tasks.models import Task,Comment
from django.contrib.auth.decorators import login_required
from rest_framework.renderers import JSONRenderer



# Create your views here.

User = get_user_model()

def homepage(request, *args, **kwargs):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user_id = request.user).order_by('created_at')
        count = len(tasks)
        comments = Comment.objects.filter(user_id = request.user)
        return render(request, 'home.html',{'tasks':tasks,'count':count,'comments':comments})
    
    return render(request,'home.html')

@login_required
def filter(request):
    if request.method == 'POST':
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        if status == "None" and priority != "None" :
            tasks = Task.objects.filter(user_id = request.user.id,priority=priority).order_by('created_at')
            count = len(tasks)
            return render(request,'home.html',{'tasks':tasks,'f_priority':priority,'count':count,'f_status':status})
        if status != "None" and priority == "None" :
            tasks = Task.objects.filter(user_id = request.user.id,status=status).order_by('created_at')
            count = len(tasks)
            return render(request,'home.html',{'tasks':tasks,'f_priority':priority,'count':count,'f_status':status})
        if status == "None" and priority == "None" :
            tasks = Task.objects.filter(user_id = request.user.id).order_by('created_at')
            count = len(tasks)
            return render(request,'home.html',{'tasks':tasks,'f_priority':priority,'count':count,'f_status':status})
        if status != "None" and priority != "None" :
            tasks = Task.objects.filter(user_id = request.user.id,status=status,priority=priority).order_by('created_at')
            count = len(tasks)
            return render(request,'home.html',{'tasks':tasks,'f_priority':priority,'count':count,'f_status':status})

