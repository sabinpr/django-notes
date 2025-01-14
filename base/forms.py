from django import forms
from .models import Note, NoteType


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'description', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Note Name', 'id': 'Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'id': 'Description', 'rows': 4}),
            'type': forms.Select(attrs={'class': 'form-control', 'id': 'Type'})
        }


class NoteTypeForm(forms.ModelForm):
    class Meta:
        model = NoteType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Note Type', 'id': 'Name'})
        }
