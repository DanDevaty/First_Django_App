from django.db import models

# Create your models here.

class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    man = models.CharField(max_length=20, default='Všichni')
    completed = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    

class User(models.Model):
    name = models.CharField(max_length=100)

