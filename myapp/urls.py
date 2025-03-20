from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("add/", views.add_todo, name="AddTodo"),
    path("add_ajax/", views.add_todo_ajax, name="add_todo_ajax"),
    path('ajax/mark-completed/', views.mark_completed, name='mark_completed_ajax'),
    path('ajax/delete-todo/', views.delete_todo, name='delete_todo_ajax'),
]
