from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    tag_id = forms.ModelChoiceField(  # Changed to ModelChoiceField for single selection
        queryset=Tag.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select rounded-0 ',
            'placeholder': 'Select tag'
        }),
        required=False,
        label=''  # Remove label for tags
    )

    class Meta:
        model = Task
        fields = ['task_detail', 'tag_id']
        widgets = {
            'task_detail': forms.Textarea(attrs={
                'class': 'form-control task-input rounded-end-0 rounded-top-0',
                'rows': 2,
                'placeholder': 'Enter task description...'
            }),
        }
        labels = {
            'task_detail': '',  # Remove label for textarea
        }