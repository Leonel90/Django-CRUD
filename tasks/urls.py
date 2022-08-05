from venv import create
from django.urls import path
from .views import create_task, list_tasks

urlpatterns = [
    path('', list_tasks),
    path('new/', create_task)
]