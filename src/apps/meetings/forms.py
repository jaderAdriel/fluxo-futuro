from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'date', 'location', 'description']
        widgets = {
            'date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%Y-%m-%dT%H:%M']
