from django.shortcuts import render

# Create your views here.
def list_tasks(request):
    return render(request, 'TasksList.html')

def create_task(request):
    print(request.data)
    return(request.POST)