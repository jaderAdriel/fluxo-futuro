from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'location', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }