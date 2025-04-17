from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Todo

# Create your views here.
class TodoListView(ListView):
    model = Todo