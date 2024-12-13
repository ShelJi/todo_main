from django.db import models


class TasksModel(models.Model):
    name = models.TextField()
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name