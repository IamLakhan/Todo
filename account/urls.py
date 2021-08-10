from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('', home_task, name='home'),
    path('add/', task_add),
    path('delete/', task_delete, name='delete'),
    path('update/', task_update, name='update'),
    path('notfound/', not_found, name='notfound')
]