from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from django.shortcuts import render

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


def index(request):
    return render(request, 'index.html')