from django import forms
from .models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['name', 'description', 'deadline', 'is_complete']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task description (optional)'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'placeholder': 'Deadline (optional)'}),
            'is_complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
