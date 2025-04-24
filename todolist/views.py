from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list_todo(request):
    # return HttpResponse('<h2><b>Home Page, Welcome Home!!!!!!!!!!</b></h2>')
    return render(request, "list_task.html")
