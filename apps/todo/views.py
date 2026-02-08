from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
import json


class IndexView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(
            owner=self.request.user,
            is_deleted=False,
            is_complete=False
        ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deleted_todos'] = Todo.objects.filter(
            owner=self.request.user,
            is_deleted=False,
            is_complete=True
        ).order_by('-created_at')
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_todos = Todo.objects.filter(owner=self.request.user, is_deleted=False)
        context['all_todos_count'] = user_todos.count()
        context['active_todos_count'] = user_todos.filter(is_complete=False).count()
        return context


@login_required
@require_http_methods(["POST"])
def add_todo_form(request):
    title = request.POST.get('title')
    if title:
        todo = Todo.objects.create(title=title, owner=request.user)
    return redirect('index')


@login_required
@require_http_methods(["POST"])
def add_todo(request):
    try:
        # Parse the incoming JSON request body
        data = json.loads(request.body)
        title = data.get('title')

        if title:
            # Create and save the todo
            todo = Todo(title=title, owner=request.user)
            todo.save()

            return JsonResponse({
                'status': 'success',
                'id': todo.id,
                'title': todo.truncated_title,
                'is_complete': todo.is_complete
            })
        else:
            return JsonResponse({'status': 'fail', 'error': 'No title provided'}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({'status': 'fail', 'error': 'Invalid JSON data'})


@login_required
@require_http_methods(["POST"])
def complete_todo(request):
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


@login_required
@require_http_methods(["POST"])
def delete_todo(request):
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
