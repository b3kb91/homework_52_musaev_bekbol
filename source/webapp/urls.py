from django.urls import path

from webapp.views import index, create_todo, todo_detail, todo_delete

urlpatterns = [
    path('', index),
    path('create/', create_todo),
    path('todo/', todo_detail),
    path('delete/', todo_delete)
]
