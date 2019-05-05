from api.models import TaskList, Task
from api.serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def tasklist_tasks(request, tasklist_name):
    try:
        tasklist = TaskList.objects.get(name=tasklist_name)
    except TaskList.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_200_OK)

    tasks = tasklist.task_set.all()

    if request.method == 'GET':
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':

        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if tasks.get(name=request.data['name']):
            return Response("There is already task with the same name in this task list",
                            status=status.HTTP_306_RESERVED)

        serializer.save()
        return Response(serializer.data, status=201)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, tasklist_name, task_name):
    try:
        tasklist = TaskList.objects.get(name=tasklist_name)
    except TaskList.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_200_OK)

    try:
        task = Task.objects.get(name=task_name, tasklist_id=tasklist.id)
    except Task.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_200_OK)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TaskSerializer(instance=task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        task.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)