from dataclasses import fields
from logging import NOTSET
from turtle import title
from django.core.exceptions import ValidationError
from django import forms

from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'notes')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'notes': forms.Textarea(attrs={'class': 'form-control mb'})  

        }
        labels = {
            'notes' : "Write your thought here:" 
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('We only accept notes about Django')
        return title