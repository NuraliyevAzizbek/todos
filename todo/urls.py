from django.urls import path

from . import views

urlpatterns = [
    path("", views.todo, name="todo"),
    path("update/<int:pk>", views.todo_update, name="update"),
    path("delete/<int:pk>", views.todo_delete, name="delete"),
    path("isdone/<int:pk>", views.todo_isdone, name="isdone"),
]
