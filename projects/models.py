from django.db import models
from time import time
from django.conf import settings

# Create your models here.
class Project(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="projects")
    name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    
    def __str__(self):
             return self.name
   
 