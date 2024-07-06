from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    STATUS_CHOISES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress '),
        ('completed', 'Completed'), 
    ]
    PRIORY_CHOISES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]


    title = models. CharField(max_length=100)
    description = models. TextField()
    status = models. CharField(max_length=20, choices=STATUS_CHOISES, default='pending')
    priority = models. CharField(max_length=20, choices=PRIORY_CHOISES, default='low')
    due_date= models. DateField()
    user = models.ForeignKey (User, on_delete=models.CASCADE)

    def __str__(self):
        return  self.title
    

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text



















