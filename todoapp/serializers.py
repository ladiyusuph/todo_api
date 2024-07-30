from rest_framework import serializers
from .models import TodoList
from accounts.serializers import UserSerializer


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['id', 'task', 'description', 'completed']
        read_only_fields = ['owner']