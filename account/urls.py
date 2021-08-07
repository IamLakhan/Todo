from django.contrib import admin
from django.urls import path, include
from .views import login_user, logout_user, register_user, home_task, task_add, task_delete, task_update

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('', home_task, name='home'),
    path('add/', task_add),
    path('delete/', task_delete, name='delete'),
    path('update/', task_update, name='update'),
]