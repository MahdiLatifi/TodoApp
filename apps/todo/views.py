from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Todo


# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/auth/login')
def index(request):
    todos = Todo.objects.filter(owner=request.user).order_by('is_complete').order_by('-created_at')
    return render(request, 'index.html', {'todos': todos})


@login_required(login_url='http://127.0.0.1:8000/auth/login')
def profile(request):
    return render(request, "profile.html")


@login_required(login_url='http://127.0.0.1:8000/auth/login')
def add_todo(request):
    print(request.POST)
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            todo = Todo(title=title, owner=request.user)
            todo.save()
            return redirect('/')
        return JsonResponse({'status': 'fail'})
