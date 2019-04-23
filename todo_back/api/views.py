import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer


# Create your views here.

@csrf_exempt
def tasklist_list(request):
    if request.method == 'GET':
        tasklists = TaskList.objects.all()
        json_tasklists = [tl.to_json() for tl in tasklists]
        return JsonResponse(json_tasklists, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=201)

@csrf_exempt
def tasklist_detail(request, tasklist_name):
    try:
        tasklist = TaskList.objects.get(id=tasklist_name)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer(tasklist)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=tasklist, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        tasklist.delete()
        return JsonResponse({}, status=204)
