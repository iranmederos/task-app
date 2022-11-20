from django.db import models
from authentication.models import CustomUser
# Create your models here.

#modelo para hacer las prioridades de las tareas
class Priority(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.name}'


#modelo para crear las tareas de cada usuario
class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, null=False)
    description = models.CharField(max_length=150, null = True, blank = True)
    is_completed = models.BooleanField(default=False)
    priority = models.ForeignKey(Priority, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.title} - {self.user}"