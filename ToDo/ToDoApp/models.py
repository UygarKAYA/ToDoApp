from django.db import models

# Create your models here.
class ToDoApp(models.Model):
    title = models.CharField(max_length=25, verbose_name='Title')
    description = models.CharField(max_length=50, verbose_name='Description')
    isComplated = models.BooleanField(verbose_name='isCompleted')

    def __str__(self):
        return self.title