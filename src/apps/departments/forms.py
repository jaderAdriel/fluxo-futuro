from django import forms
from .models import Department
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from config.utils import translate_permission


class DepartmentForm(forms.ModelForm):

    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, **kwargs)

        
        # troca as labels exibidas dentro dos campos de seleção
        self.fields['permissions'].label_from_instance = self.label_permissoes
        self.fields['members'].label_from_instance = self.label_members

        # remove as permissões padrão do Django
        self.fields['permissions'].queryset = Permission.objects.filter(id__gte=25).exclude(codename__contains='token')

        self.fields['members'].queryset = User.objects.filter(is_active=True)


    def label_permissoes(self, obj):
        return translate_permission(obj)


    def label_members(self, obj):
        return f"{obj.username} ({obj.email})"

    class Meta:
        model = Department
        fields = ['name', 'members', 'is_active', 'permissions']

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Informe o nome do Departmento.'}
            ),
            'members': forms.SelectMultiple(attrs={'class': 'select-multiple w-full'}),
            'permissions': forms.CheckboxSelectMultiple(
                attrs={'class': 'switch-input form-check-input'}
            ),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),            
        }
        
        labels = {
            'name': 'Nome',
            'permissions': 'Permissões',
        }


class DeleteDepartmentForm(DepartmentForm):
    def __init__(self, *args, **kwargs):

        super(DeleteDepartmentForm, self).__init__(*args, **kwargs)
        
        for f in self.fields:
            self.fields[f].widget.attrs['disabled'] = True
