from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from apps.departments.models import Department
from config.utils import translate_permission

class UserForm(forms.ModelForm):

    departments = forms.ModelMultipleChoiceField(
        queryset=Department.objects.filter(is_active=True),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'select-multiple w-full',
        })
    )

    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.filter(id__gte=25).exclude(codename__contains='token'),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'switch-input form-check-input',
            'data-placeholder': 'Selecione os setores',
        })
    )

    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, **kwargs)

        # troca as labels exibidas dentro dos campos de seleção
        self.fields['permissions'].label_from_instance = self.label_permissoes

    def label_permissoes(self, obj):
        return translate_permission(obj)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'last_name', 'email', 'is_active', 'is_superuser']

        widgets = {
            'username': forms.TextInput( attrs={'class': 'form-control'}),
            'first_name': forms.TextInput( attrs={'class': 'form-control'}),
            'last_name': forms.TextInput( attrs={'class': 'form-control'}),
            'email': forms.TextInput( attrs={'class': 'form-control'}),
            'departments': forms.SelectMultiple(attrs={'class': 'select-multiple w-full'}),
            'permissions': forms.CheckboxSelectMultiple(
                attrs={'class': 'switch-input form-check-input'}
            ),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),            
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),            
        }
        
        labels = {
            'is_superuser': 'É admin',
        }

    def save(self, commit=True):
        user: User = super().save(commit=commit)
        perms = self.cleaned_data.get('permissions')
        if perms is not None:
            user.user_permissions.set(perms)

        depts = self.cleaned_data.get('departments')
        user.member_department.clear()
        if depts is not None:
            for dep in depts:
                Department.objects.get(pk=dep.pk).members.add(user)

        return user


class DeleteUserForm(UserForm):
    def __init__(self, *args, **kwargs):

        super(DeleteUserForm, self).__init__(*args, **kwargs)
        
        for f in self.fields:
            self.fields[f].widget.attrs['disabled'] = True
