from django.shortcuts import render, HttpResponse, redirect
from .models import ToDoItem
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = ToDoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def add_todo(request):
    return render(request, "add_todo.html")

# Funkce pro přidání úkolu pomocí AJAX
def add_todo_ajax(request):
    if request.method == "POST":
        title = request.POST.get('title')  # Získání názvu úkolu
        deadline = request.POST.get('deadline')  # Získání datumu splnění
        if title or deadline:  # Pokud název není prázdný
            task = ToDoItem.objects.create(title=title, deadline=deadline, completed=False)  # Vytvoření nového úkolu
            task.save()
            return JsonResponse({"status": "success", "task_id": task.id, "title": task.title})
        return JsonResponse({"status": "error", "message": "Title is required"})
    return JsonResponse({"status": "error", "message": "Invalid request"})

def mark_completed(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        try:
            task = ToDoItem.objects.get(id=task_id)
            task.completed = True
            task.save()
            return JsonResponse({"status": "success", "task_id": task.id, "completed": task.completed})
        except ObjectDoesNotExist:
            return JsonResponse({"status": "error", "message": "Task not found"})
    return JsonResponse({"status": "error", "message": "Invalid request method"})

def delete_todo(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        try:
            task = ToDoItem.objects.get(id=task_id)
            task.delete()
            return JsonResponse({"status": "success", "task_id": task_id})
        except ObjectDoesNotExist:
            return JsonResponse({"status": "error", "message": "Task not found"})
    return JsonResponse({"status": "error", "message": "Invalid request method"})      
        