from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    due_date = models.DateTimeField()

    prority_choices = [
        ('low','low'),
        ('medium','medium'),
        ('high','high'),
    ]
    priority = models.CharField(max_length=15,choices=prority_choices,default='medium')

    category_choices = [
        ('personal','personal'),
        ('work','work'),
        ('learning','learning'),
    ]
    category = models.CharField(max_length=15,choices=category_choices, default='personal')

    status_choices = [
        ('pending','pending'),
        ('in-progress','in-progress'),
        ('completed','completed'),
    ]
    status = models.CharField(max_length=15,choices=status_choices,default='pending')

    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Collaborator(models.Model):
    id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField()
