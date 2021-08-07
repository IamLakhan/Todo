from django.contrib import admin
from django.urls import path, include
from .views import login_user, logout_user, home_task, task_add

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', home_task, name='home'),
    path('add/', task_add),
]