from django import forms
from first_app.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        exclude = ['is_completed']