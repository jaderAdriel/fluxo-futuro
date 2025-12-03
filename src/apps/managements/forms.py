from django import forms
from .models import Unidade

# Formulário principal para criação e edição de Gestões
class ManagementForm(forms.ModelForm):
    class Meta:
        model = Unidade  # Modelo associado ao formulário
        fields = ['name', 'begin_date', 'end_date']  # Campos que serão exibidos no formulário

        # Widgets personalizados para estilização e placeholders
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'begin_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
        }


# Formulário para confirmação de exclusão da Gestão
class DeleteManagementForm(ManagementForm):

    def __init__(self, *args, **kwargs):
        super(DeleteManagementForm, self).__init__(*args, **kwargs)
        
        # Desabilita todos os campos do formulário para exibição somente leitura (confirmação de exclusão)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True
