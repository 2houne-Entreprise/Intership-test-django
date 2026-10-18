from django.utils import timezone
from django.db import models
from projects.models import Project

# Create your models here.

        
class TaskQuerySet(models.QuerySet):
    def overdue(self):
        return (
            self.filter(deadline__lt=timezone.localdate())
            .exclude(status="done")
        )

class Task(models.Model):
    class Status(models.TextChoices):
        PENDING="pending","En attente"
        IN_PROGRESS="in_progress","En cours"
        DONE="done","Terminee"
        
    project=models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    deadline=models.DateField(null=True,blank=True)
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status = models.CharField(
           max_length=20,
           choices=Status.choices,
           default=Status.PENDING,
       )


       
       
    objects = TaskQuerySet.as_manager()
    @property
    def status_label(self):
        return self.get_status_display()
        
    def __str__(self):
        return self.title


