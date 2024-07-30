from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoListSerializer
from .models import TodoList


@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_todotask(request):
    serializer = TodoListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(
            {"Message": "Task Created Successfully", "Task": serializer.data}
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_todotask(request, pk):
    task = TodoList.objects.filter(owner=request.user).get(pk=pk)
    serializer = TodoListSerializer(task, request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)

    return Response({"Message": "Task Updated", "task": serializer.data})


@api_view(["DELETE"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_task(request, pk):
    task = TodoList.objects.filter(owner=request.user).get(pk=pk)
    task.delete()

    return Response({"Message": "Task Deleted"})


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def all_tasks(request):
    completed = request.query_params.get("completed", None)
    if completed is not None:
        tasks = TodoList.objects.filter(completed=completed)
    else:
        tasks = TodoList.objects.all()
    serializer = TodoListSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_task(request, pk):
    task = get_object_or_404(TodoList,pk=pk)
    serializer = TodoListSerializer(task)
    
    return Response(serializer.data)