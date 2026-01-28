from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Todo
import json


@login_required
def index(request):
    todos = Todo.objects.filter(is_deleted=False)
    todos = todos.filter(owner=request.user).order_by('-created_at')
    deleted_todos = todos.filter(is_complete=True)
    todos = todos.filter(is_complete=False)
    return render(request, 'index.html', {'todos': todos, 'deleted_todos': deleted_todos})


@login_required
def profile(request):
    user = request.user
    todos = Todo.objects.filter(is_deleted=False)
    active_todos_count = todos.filter(is_complete=False).count()
    return render(request, "profile.html", {'user': user, 'todos': todos, 'active_todos_count': active_todos_count})


@login_required
def add_todo(request):
    if request.method == "POST":
        try:
            # Parse the incoming JSON request body
            try:
                my_method = 'js'
                data = json.loads(request.body)
                title = data.get('title')
            except:
                title = request.POST.get('title')
                my_method = 'enter'

            if title:
                # Create and save the todo
                todo = Todo(title=title, owner=request.user)
                todo.save()

                return JsonResponse({
                    'status': 'success',
                    'id': todo.id,
                    'title': todo.truncated_title,
                    'is_complete': todo.is_complete
                }) if my_method == 'js' else redirect(reverse('index'))
            else:
                return JsonResponse({'status': 'fail', 'error': 'No title provided'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'fail', 'error': 'Invalid JSON data'})

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
                'title': todo.truncated_title,
                'is_complete': todo.is_complete
            })

        return JsonResponse({'status': 'fail', 'error': 'Todo ID not provided'})

    return JsonResponse({'status': 'fail', 'error': 'Invalid request method'})


@login_required
def delete_todo(request):
    if request.method == "POST":
        data = json.loads(request.body)
        todo_id = data.get('id')

        if todo_id:
            todo = get_object_or_404(Todo, pk=todo_id, owner=request.user)
            todo.is_deleted = True
            todo.save()

            return JsonResponse({
                'status': 'success',
            })

        return JsonResponse({'status': 'fail', 'error': 'Todo ID not provided'})

    return JsonResponse({'status': 'fail', 'error': 'Invalid request method'})
