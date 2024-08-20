from django.shortcuts import render

# Create your views here.
def list_tasks(request):
    retunr render('TasksList.html')