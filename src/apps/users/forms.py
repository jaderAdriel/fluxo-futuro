from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from apps.departments.models import Department
from config.utils import translate_permission
from django.contrib.auth.password_validation import validate_password

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

    # Campo para confirmação de senha
    password2 = forms.CharField(
        required=False,
        label="Confirmação senha",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Senha confirmação',
        }),
        validators=[validate_password]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # troca as labels exibidas dentro dos campos de seleção
        self.fields['permissions'].label_from_instance = self.label_permissoes

        if self.instance and self.instance.pk:
            self.fields.pop('password', None)
            self.fields.pop('password2', None)


    def label_permissoes(self, obj):
        return translate_permission(obj)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'last_name', 'email', 'is_active', 'is_superuser', 'password']

        widgets = {
            'username': forms.TextInput( attrs={'class': 'form-control','autocomplete': 'off'}),
            'password': forms.PasswordInput( attrs={'class': 'form-control', 'autocomplete': 'off'},),
            'first_name': forms.TextInput( attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'last_name': forms.TextInput( attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'email': forms.TextInput( attrs={'class': 'form-control', 'autocomplete': 'off'}),
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

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        
        if password and password != password2:
            # 4. Adiciona o erro especificamente no campo senha2
            self.add_error('password2', 'As senhas não coincidem')

    def save(self, commit=True):
        
        user: User = super().save(commit=False)

        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)

        if commit:
            user.save()


        perms = self.cleaned_data.get('permissions')
        if perms is not None:
            user.user_permissions.set(perms)

        depts = self.cleaned_data.get('departments')
        
        if depts is not None:
            for dep in depts:
                Department.objects.get(pk=dep.pk).members.add(user)

        return user


class DeleteUserForm(UserForm):
    def __init__(self, *args, **kwargs):

        super(DeleteUserForm, self).__init__(*args, **kwargs)
        
        for f in self.fields:
            self.fields[f].widget.attrs['disabled'] = True
