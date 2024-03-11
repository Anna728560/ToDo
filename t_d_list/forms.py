from django import forms

from .models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    deadline_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Task
        fields = "__all__"
