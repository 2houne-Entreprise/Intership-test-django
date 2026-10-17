from django import forms

from TaskManager.models import Task




class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=["title","status","deadline"]

        widgets={
            "title": forms.TextInput(attrs={
                     "placeholder": "Titre de la tache",
                     "maxlength": 255,
                 }),
                 "status": forms.Select(),
                 "deadline": forms.DateInput(attrs={
                     "type": "date",
                 }),
        }
    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
    
        if not title:
            raise forms.ValidationError( "Le titre de la tache est obligatoire")
    
        if len(title) > 255:
            raise forms.ValidationError("Le titre ne doit pas depasser 255 caracteres")
    
        return title    