from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Todo
import json


@login_required
def index(request):
    todos = Todo.objects.filter(owner=request.user).order_by('is_complete')
    return render(request, 'index.html', {'todos': todos})


@login_required
def profile(request):
    return render(request, "profile.html")


@login_required
def add_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            todo = Todo(title=title, owner=request.user)
            todo.save()
            return redirect(reverse('index'))
        return JsonResponse({'status': 'fail', 'error': 'No title provided'})

    return JsonResponse({'status': 'fail', 'error': 'Invalid request method'})


@login_required
def complete_todo(request):
    if request.method == "POST":
        data = json.loads(request.body)
        todo_id = data.get('id')

        if todo_id:
            todo = get_object_or_404(Todo, pk=todo_id, owner=request.user)
            todo.is_complete = not todo.is_complete
            todo.save()

            return JsonResponse({
                'status': 'success',
                'id': todo.id,
                'title': todo.title,
                'is_complete': todo.is_complete
            })

        return JsonResponse({'status': 'fail', 'error': 'Todo ID not provided'})

    return JsonResponse({'status': 'fail', 'error': 'Invalid request method'})
