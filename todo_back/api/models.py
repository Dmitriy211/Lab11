from django.db import models


# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    status = models.CharField(max_length=20)
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created': self.created_at,
            'due': self.due_on,
            'status': self.status,
            'task_list_name': self.task_list.name
        }
