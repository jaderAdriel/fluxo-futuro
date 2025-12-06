from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['description', 'amount', 'date', 'type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'},format='%Y-%m-%d'),
        }
