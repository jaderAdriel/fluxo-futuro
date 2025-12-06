from django.shortcuts import render, redirect, get_object_or_404
from .models import Meeting
from .forms import MeetingForm


# Listar reuniões
def index(request):
    meetings = Meeting.objects.all().order_by('-date')
    return render(request, 'pages/meetings/index.html', {'meetings': meetings})


# Detalhar reunião
def detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)
    return render(request, 'pages/meetings/detail.html', {'meeting': meeting})


# Criar nova reunião
def create(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-meetings')
    else:
        form = MeetingForm()

    context = {
        "form": form,
        "is_create": True,
    }
    return render(request, 'pages/meetings/form.html', context=context)


# Editar reunião
def edit(request, id):
    meeting = get_object_or_404(Meeting, id=id)

    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('list-meetings')
    else:
        form = MeetingForm(instance=meeting)

    context = {
        "form": form,
        "is_edit": True,  # Mudei de is_delete pra is_edit pra fazer sentido, mas segue seu padrão
    }
    return render(request, 'pages/meetings/form.html', context=context)


# Deletar reunião
def delete(request, id):
    meeting = get_object_or_404(Meeting, id=id)

    if request.method == 'POST':
        meeting.delete()
        return redirect('list-meetings')

    context = {
        "meeting": meeting,
        "is_delete": True,
    }
    return render(request, 'pages/meetings/form.html', context=context)
