from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.urls import reverse

from apps.departments.signals import atualizar_usuarios_no_grupo

from .models import Department
from .forms import DepartmentForm, DeleteDepartmentForm


# Listar gestões
@login_required
@permission_required("departments.view_department", raise_exception=True)
def index(request):

    department_list = Department.objects.all()

    context = {
        "department_list": department_list
    }

    return render(request, 'pages/departments/index.html', context)


# Detalhar gestão
@login_required
@permission_required("departments.view_department", raise_exception=True)
def detail(request, id):
    department = get_object_or_404(Department, pk=id)

    context = {
        "department": department
    }

    return render(request, 'pages/departments/detail.html', context)


# Criar nova gestão
@login_required
@permission_required("departments.add_department", raise_exception=True)
def create(request):

    form = DepartmentForm()

    if request.method == 'POST':
        form = DepartmentForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            form.save_m2m()
            atualizar_usuarios_no_grupo(instance)
            messages.success(request, "Departamento criada com sucesso")
            return redirect(reverse('list-departments'))
        else:
            messages.error(request, "Erro ao criar departamento")

    context = {
        "is_create": True,
        "form": form
    }
    return render(request, 'pages/departments/form.html', context=context)


# Editar gestão
@login_required
@permission_required("departments.change_department", raise_exception=True)
def edit(request, id):

    department = get_object_or_404(Department, pk=id)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)

        if form.is_valid():
            department = form.save()
            atualizar_usuarios_no_grupo(department)
            messages.success(request, "Departamento criada com sucesso")
            return redirect(reverse('list-departments'))
        else:
            messages.error(request, "Erro ao editar departamento")
    else:
        form = DepartmentForm(instance=department)

    context = {
        "is_edit": True,
        "form": form
    }
    return render(request, 'pages/departments/form.html', context=context)


# Deletar gestão
@login_required
@permission_required("departments.delete_department", raise_exception=True)
def delete(request, id):

    department = get_object_or_404(Department, pk=id)

    if request.method == 'POST':

        try:
            department.delete()
            messages.success(request, "Departamento deletada com sucesso")
            return redirect(reverse('list-departments'))
        except:
            messages.error(request, "Erro ao deletar departamento")

    form = DeleteDepartmentForm(instance=department)

    context = {
        "is_delete": True,
        "form": form
    }

    return render(request, 'pages/departments/form.html', context=context)
