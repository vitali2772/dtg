from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "index.html")

def todos(request):
    items = TodoItem.objects.all
    return render(request, "todos.html", {"todos": items})