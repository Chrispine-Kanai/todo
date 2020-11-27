from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'title': 'Home',
        'form': form
    }

    return render(request, 'tasks/lists.html', context)


def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'title': 'Update',
        'form': form
    }

    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {
        'title': 'Delete',
        'item': item
    }

    return render(request, 'tasks/delete.html', context)