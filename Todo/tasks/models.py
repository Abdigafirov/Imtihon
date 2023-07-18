from django.db import models
from django.contrib import auth
# Create your models here.


class Task(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    descript = models.TextField()
    task_created_date = models.DateTimeField()
    deadline = models.DateTimeField()

    class Meta:
        verbose_name = 'Bajariladigon ish'
        verbose_name_plural = 'Ishlar'

    def __str__(self):
        return self.title

    def get_time_deff(self):
        return self.deadline - self.task_created_date <=0