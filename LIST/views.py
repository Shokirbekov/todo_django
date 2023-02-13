from django.shortcuts import render, redirect
from .models import *

def todo(request):
    data = {
        "task": Task.objects.all(),
    }
    return render(request, 'todo.html', data)

def delete_task(request, id):
    Task.objects.get(id=id).delete()
    return redirect('/')