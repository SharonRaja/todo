from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Tag
from django.contrib.auth.models import User
from .forms import TaskForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Task, Tag
from .forms import TaskForm


# Create your views here.
def list_todo(request):
    """View to list all tasks. Along with the form to add a new task."""
    tasks = Task.objects.filter(is_done=False)
    return render(request, "list_task.html", {
        'tasks': tasks,
        'form': TaskForm()  # Add form to context
    })



def list_todo(request):
    """View to list all tasks. Along with the form to add a new task."""
    tasks = Task.objects.filter(is_done=False)
    # for task in tasks:
    #     print(f"Task ID: {task.task_id}, Task Detail: {task.task_detail}")
    return render(request, "list_task.html", {
        'tasks': tasks,
        'form': TaskForm()
    })

def add_task(request):
    """ View to add a new task. """
    if request.method == 'POST':
        try:
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                if request.user.is_authenticated:
                    task.user = request.user
                task.is_done = False
                task.save()

                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

                    if hasattr(task, 'tag'):
                        tag_data = {
                            'id': task.tag.id,
                            'tag_name': task.tag.tag_name
                        }

                    return JsonResponse({
                        'status': 'success',
                        'task': {
                            'task_id': task.task_id,
                            'task_detail': task.task_detail,
                            'is_done': task.is_done,
                            'user': task.user.username if hasattr(task, 'user') else None,
                            'tag': tag_data if hasattr(task, 'tag')  else None,
                            'created_at': task.created_at
                        }
                    }, status=200)
                return redirect('todolist:list_todo')  # Corrected namespace

            # Handle invalid form
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'error',
                    'errors': form.errors.get_json_data()
                }, status=400)

        except Exception as e:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'error',
                    'message': str(e)
                }, status=500)
            # For non-AJAX requests, redirect with error
            return redirect('todolist:list_todo')

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=400)
    

def task_complete(request, task_id):
    """ View to mark a task as complete. """
    if request.method == 'POST':
        try:
            if request.user.is_authenticated:
                task = Task.objects.get(task_id=task_id, user_id=request.user)
            else:
                task = Task.objects.get(task_id=task_id)
            task.is_done = True
            task.save()
            return JsonResponse({'status': 'success'}, status=200)
        except Task.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)
    return JsonResponse({'status': 'error'}, status=400)
