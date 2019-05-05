from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, TaskList

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        tasklist = TaskList(**validated_data)
        tasklist.save()
        return tasklist

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    tasklist_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'tasklist_id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
