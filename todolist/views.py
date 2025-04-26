from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Tag
from django.contrib.auth.models import User

# Create your views here.
def list_todo(request):
    # return HttpResponse('<h2><b>Home Page, Welcome Home!!!!!!!!!!</b></h2>')
    print('list_todo')
    tasks = Task.objects.filter(is_done=False)
    return render(request, "list_task.html", {'tasks': tasks})

def add_task(request):
    print('add_task')
    return list_todo(request)
