from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=255)
    deadline = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return(f"{self.title}")

class Task(models.Model):

    class Priority(models.TextChoices):
        HIGH = 'HI', 'High'
        MEDIUM = 'MID', 'Medium'
        LOW = 'LOW', 'Low'

    class Status(models.TextChoices):
        PENDING = 'PEND', 'Pending'
        ONGOING = 'ON', 'Ongoing'
        FINISHED = 'FIN', 'Finished'
        
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=3,
                                choices=Priority.choices, 
                                default=Priority.MEDIUM)
    status = models.CharField(max_length=4, 
                                choices=Status.choices,
                                default=Status.PENDING)
    deadline = models.DateField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return(f"{self.title}")
    
class Subtask(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PEND', 'Pending'
        ONGOING = 'ON', 'Ongoing'
        FINISHED = 'FIN', 'Finished'
        
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=4, 
                                choices=Status.choices,
                                default=Status.PENDING)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return(f"{self.title}")
    
    