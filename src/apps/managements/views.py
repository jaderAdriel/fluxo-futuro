from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from apps.managements.models import Management
from .forms import ManagementForm, DeleteManagementForm


# Listar gestões
@login_required
def index(request):

    management_list = Management.objects.all()

    context = {
        "management_list": management_list
    }

    return render(request, 'pages/managements/index.html', context)


# Detalhar gestão
@login_required
def detail(request, id):
    management = get_object_or_404(Management, pk=id)

    context = {
        "management": management
    }

    return render(request, 'pages/managements/detail.html', context)


# Criar nova gestão
@login_required
def create(request):

    form = ManagementForm()

    if request.method == 'POST':
        form = ManagementForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Gestão criada com sucesso")
            return redirect(reverse('list-managements'))
        else:
            messages.error(request, "Erro ao criar gestão")

    context = {
        "is_create": True,
        "form": form
    }
    return render(request, 'pages/managements/form.html', context=context)


# Editar gestão
@login_required
def edit(request, id):

    management = get_object_or_404(Management, pk=id)

    if request.method == 'POST':
        form = ManagementForm(request.POST, instance=management)

        if form.is_valid():
            form.save()
            messages.success(request, "Gestão criada com sucesso")
            return redirect(reverse('list-managements'))
        else:
            messages.error(request, "Erro ao editar gestão")
    else:
        form = ManagementForm(instance=management)

    context = {
        "is_edit": True,
        "form": form
    }
    return render(request, 'pages/managements/form.html', context=context)


# Deletar gestão
@login_required
def delete(request, id):

    management = get_object_or_404(Management, pk=id)

    if request.method == 'POST':

        try:
            management.delete()
            messages.success(request, "Gestão deletada com sucesso")
            return redirect(reverse('list-managements'))
        except:
            messages.error(request, "Erro ao deletar gestão")

    form = DeleteManagementForm(instance=management)

    context = {
        "is_delete": True,
        "form": form
    }

    return render(request, 'pages/managements/form.html', context=context)
