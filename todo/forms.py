from django import forms

from .models import Todo
from django.utils import timezone
from datetime import timedelta


class FilterTodoForm(forms.Form):
    filter_todo = forms.ChoiceField(
        choices=[("True", "isdone"), ("False", "isnotdone"), ("All", "all")],
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    def save(self):
        filter_todo = self.cleaned_data["filter_todo"]
        if filter_todo == "All":
            hint_filter = Todo.objects.all()
        else:
            hint_filter = Todo.objects.filter(is_done=filter_todo)
        return hint_filter


class AddTodoForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    deadline = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d",
                               attrs={'type': 'date',
                                      'min': str(timezone.now().date()),
                                      'max': str((timezone.now() + timedelta(days=365)).date())
                                      }
                                ),
        input_formats=["%d/%m/%Y", "%Y-%m-%d"],
    )


    def save(self):
        title = self.cleaned_data["title"]
        description = self.cleaned_data["description"]
        deadline = self.cleaned_data["deadline"]
        Todo.objects.create(
            title=title,
            description=description,
            deadline=deadline,
        )


class UpdateTodoForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    deadline = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d",
                               attrs={'type': 'date',
                                      'min': str(timezone.now().date()),
                                      'max': str((timezone.now() + timedelta(days=365)).date())
                                      }
                                ),
        input_formats=["%d/%m/%Y", "%Y-%m-%d"],
    )

    def save(self, pk):
        todo = Todo.objects.get(id=pk)
        todo.title = self.cleaned_data["title"]
        todo.description = self.cleaned_data["description"]
        todo.deadline = self.cleaned_data["deadline"]
        todo.save()