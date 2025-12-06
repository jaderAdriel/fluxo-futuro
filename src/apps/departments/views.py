from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from .models import Department
from .forms import DepartmentForm, DeleteDepartmentForm


# Listar gestões
@login_required
def index(request):

    department_list = Department.objects.all()

    context = {
        "department_list": department_list
    }

    return render(request, 'pages/departments/index.html', context)


# Detalhar gestão
@login_required
def detail(request, id):
    department = get_object_or_404(Department, pk=id)

    context = {
        "department": department
    }

    return render(request, 'pages/departments/detail.html', context)


# Criar nova gestão
@login_required
def create(request):

    form = DepartmentForm()

    if request.method == 'POST':
        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Gestão criada com sucesso")
            return redirect(reverse('list-departments'))
        else:
            messages.error(request, "Erro ao criar gestão")

    context = {
        "is_create": True,
        "form": form
    }
    return render(request, 'pages/departments/form.html', context=context)


# Editar gestão
@login_required
def edit(request, id):

    department = get_object_or_404(Department, pk=id)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)

        if form.is_valid():
            form.save()
            messages.success(request, "Gestão criada com sucesso")
            return redirect(reverse('list-departments'))
        else:
            messages.error(request, "Erro ao editar gestão")
    else:
        form = DepartmentForm(instance=department)

    context = {
        "is_edit": True,
        "form": form
    }
    return render(request, 'pages/departments/form.html', context=context)


# Deletar gestão
@login_required
def delete(request, id):

    department = get_object_or_404(Department, pk=id)

    if request.method == 'POST':

        try:
            department.delete()
            messages.success(request, "Gestão deletada com sucesso")
            return redirect(reverse('list-departments'))
        except:
            messages.error(request, "Erro ao deletar gestão")

    form = DeleteDepartmentForm(instance=department)

    context = {
        "is_delete": True,
        "form": form
    }

    return render(request, 'pages/departments/form.html', context=context)
