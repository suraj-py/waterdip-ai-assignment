from django.urls import path
from .views import TodoList

urlpatterns = [
    path('tasks/', TodoList.as_view()),
]
