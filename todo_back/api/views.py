from django.http import JsonResponse
from api.models import TaskList


# Create your views here.

def all_tasklists(request):
    tasklists = TaskList.objects.all()
    json_tasklists = [tl.to_json() for tl in tasklists]
    return JsonResponse(json_tasklists, safe=False)

def get_tasklist(request, tasklist_name):
    try:
        tasklist = TaskList.objects.get(name=tasklist_name)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(tasklist.to_json())
