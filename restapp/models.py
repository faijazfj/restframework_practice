from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=250)
    task_des = models.CharField(max_length=250)
    date_created=models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='Images',default="Image/None/Noimg.jpg")
