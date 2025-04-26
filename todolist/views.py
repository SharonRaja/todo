from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Tag
from django.contrib.auth.models import User
from .forms import TaskForm

# Create your views here.
def list_todo(request):
    tasks = Task.objects.filter(is_done=False)
    return render(request, "list_task.html", {
        'tasks': tasks,
        'form': TaskForm()  # Add form to context
    })

from django.shortcuts import render, redirect
from .models import Task, Tag
from .forms import TaskForm

def list_todo(request):
    """View to list all tasks. Along with the form to add a new task."""
    tasks = Task.objects.filter(is_done=False)
    return render(request, "list_task.html", {
        'tasks': tasks,
        'form': TaskForm()
    })

def add_task(request):
    """ View to add a new task. """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if request.user.is_authenticated:
                task.user = request.user
            task.is_done = False
            
            # print("Saved task with tag:", task.tag_id)  # Verify tag is attached
            task.save()
            # form.save_m2m()
            return redirect('todolist:list_todo')  # Corrected namespace
    
    return list_todo(request)
