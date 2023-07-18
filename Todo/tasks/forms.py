from django.forms import ModelForm,Textarea, TextInput, DateTimeField,DateTimeInput
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'descript', 'deadline', 'author']

class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'descript', 'author', 'task_created_date', 'deadline']
        context = {
            'title': TextInput(),
            'descript': Textarea(),
            'task_created_date':DateTimeInput(attrs={'placeholder':"YYYY-MM-DD HH:MM:SS"}),
            'deadline': DateTimeInput(attrs={'placeholder':"YYYY-MM-DD HH:MM:SS"})
        }