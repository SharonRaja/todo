from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Tag
from django.contrib.auth.models import User

print("hello world")
# Create your views here.
def list_todo(request):
    # return HttpResponse('<h2><b>Home Page, Welcome Home!!!!!!!!!!</b></h2>')
    print('list_todo')
    tasks = Task.objects.filter(is_done=False)
    for task in tasks:
        print(task.task_detail, task.is_done, task.tag_id.tag_name, task.user_id.username, task.created_at)
    return render(request, "list_task.html", {'tasks': tasks})
