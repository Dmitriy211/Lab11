from api.models import TaskList
from api.serializers import TaskListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

# FBV

@api_view(['GET', 'POST'])
def tasklist_list(request):
    if request.method == 'GET':
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer(tasklists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

@api_view(['GET', 'PUT', 'DELETE'])
def tasklist_detail(request, tasklist_name):
    try:
        tasklist = TaskList.objects.get(name=tasklist_name)
    except TaskList.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_200_OK)

    if request.method == 'GET':
        serializer = TaskListSerializer(tasklist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TaskListSerializer(instance=tasklist, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        tasklist.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

# CBV

class TaskListList(APIView):
    def get(self, request):
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer(tasklists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class TaskListDetail(APIView):
    def get_object(self, tasklist_name):
        try:
            return TaskList.objects.get(name=tasklist_name)
        except TaskList.DoesNotExist as e:
            raise Http404 #return Response({'error': str(e)}, status=status.HTTP_200_OK)

    def get(self, request, tasklist_name):
        tasklist = self.get_object(tasklist_name)
        serializer = TaskListSerializer(tasklist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, tasklist_name):
        tasklist = self.get_object(tasklist_name)
        serializer = TaskListSerializer(instance=tasklist, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, tasklist_name):
        tasklist = self.get_object(tasklist_name)
        tasklist.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
