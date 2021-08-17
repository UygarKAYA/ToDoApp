from django.shortcuts import render
from django.shortcuts import redirect

from .models import ToDoApp

# Create your views here.
def index(request):
    todo = ToDoApp.objects.all()
    return render(request, 'index.html', {'todo': todo})

def addToDo(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        title = request.POST.get('Title')
        description = request.POST.get('Description')

        newToDoAppList = ToDoApp(title = title, description = description, isComplated = False)
        newToDoAppList.save()

        return redirect('/')

def updateToDo(request, ID):
    todo = ToDoApp.objects.filter(id = ID).first()
    todo.isComplated = not todo.isComplated
    todo.save()

    return redirect('/')


def deleteToDo(request, ID):
    todo = ToDoApp.objects.filter(id = ID)
    todo.delete()

    return redirect('/')
