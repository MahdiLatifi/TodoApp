from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
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
        # 'todos': todos, 'active_todos_count': active_todos_count
        context['all_todos_count'] = Todo.objects.filter(owner=self.request.user, is_deleted=False).count()
        context['active_todos_count'] = Todo.objects.filter(owner=self.request.user, is_deleted=False,
                                                            is_complete=False).count()
        return context


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
