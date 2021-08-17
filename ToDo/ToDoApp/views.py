from django.shortcuts import render
from django.shortcuts import redirect

from .models import ToDoApp

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addToDo(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        title = request.POST.get('Title')
        description = request.POST.get('Description')

        newToDoAppList = ToDoApp(title = title, description = description, isComplated = False)
        newToDoAppList.save()

        return redirect('/')
