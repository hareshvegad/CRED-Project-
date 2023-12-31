from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=555)
    description=models.TextField()
    completed=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=2)

def __str__(self):
    return self.title