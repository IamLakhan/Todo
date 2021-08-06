from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
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

def home_task(request):
    return render(request, 'index.html')