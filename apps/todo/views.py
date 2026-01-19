from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/auth/login')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='http://127.0.0.1:8000/auth/login')
def profile(request):
    return render(request, "profile.html")
