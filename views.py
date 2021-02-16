from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import TaskSerializer
from .models import Task
# Create your views here.



@api_view(['GET'])
def newindex(request):
    urls = {
        't1' : 'eat/',
        't2' : 'sleep/',
        't3' : 'drink/',
        't4' : 'run/',
    }

    return Response(urls)

@api_view(['GET'])
def tasklist(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def one(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def add(request):
   
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item successfully deleted")

