from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from . models import Task

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task,pk = pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task,pk = pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request,pk):
    task = get_object_or_404(Task,pk = pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task,
        }
        return render(request,'editTask.html',context)
    
def deleteTask(request,pk):
    task = get_object_or_404(Task,pk = pk)
    task.delete()
    return redirect('home')







# Create your views here.
