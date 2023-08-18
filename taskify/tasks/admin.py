from django.contrib import admin
from .models import Task,Collaborator,Comment
# Register your models here.

admin.site.register(Task)
admin.site.register(Collaborator)
admin.site.register(Comment)