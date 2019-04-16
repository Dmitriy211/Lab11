from django.db import models


# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

    def to_json(self):
        return {
            'name': self.name
        }
