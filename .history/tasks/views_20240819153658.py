from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'TasksList.html', {'tasks': tasks})

def create_task(request):
    task = Task(tittle=request.POST['tittle'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    return redirect('/tasks/')