from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Nom du projet",
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Description du projet",
                "rows": 4,
            }),
        }



        