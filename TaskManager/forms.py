from django import forms
from TaskManager.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        max_length=255,
        error_messages={
            "required": "Le titre de la tâche est obligatoire.",
            "max_length": "Le titre ne doit pas dépasser 255 caractères.",
        },
        widget=forms.TextInput(attrs={
            "placeholder": "Titre de la tâche",
            "maxlength": 255,
        }),
    )

    class Meta:
        model = Task
        fields = ["title", "status", "deadline", "attachment"]

        widgets = {
            "status": forms.Select(),
            "deadline": forms.DateInput(attrs={
                "type": "date",
            }),
            "attachment": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()

        if not title:
            raise forms.ValidationError(
                "Le titre de la tâche est obligatoire."
            )

        return title