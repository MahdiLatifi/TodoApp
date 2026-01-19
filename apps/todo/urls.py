from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('addTodo/', views.add_todo, name='add_todo'),
    path('completeTodo/', views.complete_todo, name='complete_todo'),
]
