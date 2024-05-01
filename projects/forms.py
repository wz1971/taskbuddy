from django import forms
from django.contrib.auth.models import User
from .models import Task

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class TaskSearchForm(forms.Form):
    title = forms.CharField(
        max_length=50, required=True, label="Enter task title"
    )
    status = forms.ChoiceField(choices=Task.Status.choices)
    priority = forms.ChoiceField(choices=Task.Priority.choices)
