from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth.models import User

from django.urls import reverse
from .forms import UserForm, DeleteUserForm


# Listar usuários
@login_required
@permission_required("users.view_user", raise_exception=True)
def index(request):

    user_list = User.objects.all()

    context = {
        "user_list": user_list
    }

    return render(request, 'pages/users/index.html', context)


# Detalhar usuário
@login_required
@permission_required("users.view_user", raise_exception=True)
def detail(request, id):
    user = get_object_or_404(User, pk=id)

    context = {
        "user": user
    }

    return render(request, 'pages/users/detail.html', context)


@login_required
@permission_required("users.add_user", raise_exception=True)
def create(request):

    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criada com sucesso")
            return redirect(reverse('list-users'))
        else:
            messages.error(request, "Erro ao criar usuário")

    context = {
        "is_create": True,
        "form": form
    }
    return render(request, 'pages/users/form.html', context=context)


# Editar usuário
@login_required
@permission_required("users.change_user", raise_exception=True)
def edit(request, id):

    user = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criada com sucesso")
            return redirect(reverse('list-users'))
        else:
            messages.error(request, "Erro ao editar usuário")
    else:
        departments = user.member_department.all()
        permissions = user.user_permissions.all()
        form = UserForm(instance=user, initial={
            "departments": departments,
            "permissions": permissions
        })

    context = {
        "is_edit": True,
        "form": form
    }
    return render(request, 'pages/users/form.html', context=context)


# Deletar usuário
@login_required
@permission_required("users.delete_user", raise_exception=True)
def delete(request, id):

    user = get_object_or_404(User, pk=id)

    if request.method == 'POST':

        try:
            user.delete()
            messages.success(request, "Usuário deletada com sucesso")
            return redirect(reverse('list-users'))
        except:
            messages.error(request, "Erro ao deletar usuário")

    form = DeleteUserForm(instance=user)

    context = {
        "is_delete": True,
        "form": form
    }

    return render(request, 'pages/users/form.html', context=context)
