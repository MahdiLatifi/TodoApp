from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.
def login_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return redirect(reverse('index'))
        else:
            login_form = AuthenticationForm()
            return render(request, 'registration/login.html', {'login_form': login_form, 'errors': form.errors})
    login_form = AuthenticationForm()
    return render(request, 'registration/login.html', {'login_form': login_form})


@login_required(login_url='http://127.0.0.1:8000/auth/login')
def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect(reverse('auth:login'))
        else:
            signup_form = UserCreationForm()
            return render(request, 'registration/signup.html', {'signup_form': signup_form, 'errors': form.errors})
    signup_form = UserCreationForm()
    return render(request, 'registration/signup.html', {'signup_form': signup_form})


@login_required
def complete_profile(request):
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get('name')
        last_name = request.POST.get('lastname')
        if first_name and last_name:
            user.first_name = first_name
            user.last_name = last_name
            user.save()
    return redirect(reverse('profile'))
