from django.urls import path

from webapp.views import index, create_todo, todo_detail, todo_delete

urlpatterns = [
    path('', index, name='todo'),
    path('create/', create_todo, name='todo_create'),
    path('todo/<int:pk>/', todo_detail, name="todo_detail"),
    path('delete/<int:pk>/', todo_delete, name="todo_delete"),
]
