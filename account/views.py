from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Task

import datetime
# Create your views here.
def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    print(user, username, password)
    if user:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'login.html', {'error':True, 'message':'Please check your credentials!'})

def logout_user(request):
    logout(request)
    return redirect('/')

def register_user(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return redirect('login')

def home_task(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        context = {'tasks':tasks}
        return render(request, 'index.html', context)
    return redirect('login')

def task_add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    title = request.POST.get('title')
    description = request.POST.get('description')
    time = datetime.datetime.now()
    task = Task(title=title, description=description, created_at=time, user=request.user)
    task.save()
    return redirect('/')