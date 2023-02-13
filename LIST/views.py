from django.shortcuts import render
from .models import *

def todo(request):
    data = {
        "task": Task.objects.all(),
    }
    return render(request, 'todo.html', data)