from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('index/',views.newindex, name = "newindex_page"),
    path('list/',views.tasklist, name = "tasklist"), 
    path('one/<str:pk>/',views.one, name = "taskone"),  
    path('add/',views.add, name = "taskadd"),
    path('update/<str:pk>/',views.update, name = "task"),
    path('delete/<str:pk>',views.delete, name = "delete"),
    
]
