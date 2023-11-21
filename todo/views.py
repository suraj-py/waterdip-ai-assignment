from django.shortcuts import render
from .models import Todo
from rest_framework import generics
from .serializer import TodoSerializer

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

