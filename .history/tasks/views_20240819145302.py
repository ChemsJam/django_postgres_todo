from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request):
    return render(request, 'TasksList.html')

def create_task(request):
    Task(title=request.POST['tittle'], description=request.POST['description'])
    Task.save
    return redirect ('/tasks/')