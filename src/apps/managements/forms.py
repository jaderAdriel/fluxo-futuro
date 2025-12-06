from django import forms
from .models import Management
from config.form import BaseStyledForm

# Formulário principal para criação e edição de Gestões
class ManagementForm(BaseStyledForm):
    class Meta:
        model = Management  # Modelo associado ao formulário
        fields = ['name', 'begin_date', 'end_date']  # Campos que serão exibidos no formulário

        # Widgets personalizados para estilização e placeholders
        widgets = {
            'name': forms.TextInput(),
            'begin_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


# Formulário para confirmação de exclusão da Gestão
class DeleteManagementForm(ManagementForm):

    def __init__(self, *args, **kwargs):
        super(DeleteManagementForm, self).__init__(*args, **kwargs)
        
        # Desabilita todos os campos do formulário para exibição somente leitura (confirmação de exclusão)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True
