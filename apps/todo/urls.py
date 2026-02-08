from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('addTodo/', views.add_todo, name='add_todo'),
    path('addTodoForm/', views.add_todo_form, name='add_todo_form'),
    path('completeTodo/', views.complete_todo, name='complete_todo'),
    path('deleteTodo/', views.delete_todo, name='delete_todo'),
]
