from django import forms
from .models import Task

prority_choices = [
        ('low','low'),
        ('medium','medium'),
        ('high','high'),
    ]
category_choices = [
        ('personal','personal'),
        ('work','work'),
        ('learning','learning'),
    ]
status_choices = [
        ('pending','pending'),
        ('in-progress','in-progress'),
        ('completed','completed'),
    ]
class AddTask(forms.Form):
    title = forms.CharField(
     
    )
    description = forms.CharField(
       
    )
    priority = forms.ChoiceField(
        choices = prority_choices, 
       
    )
    status = forms.ChoiceField(choices = status_choices, )
    due_date = forms.DateTimeField()

 