from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required("events.view_event", raise_exception=True)
def list_events(request):
    events = Event.objects.all()
    return render(request, 'pages/events/index.html', {'events': events})


@login_required
@permission_required("events.add_event", raise_exception=True)
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-events')
    else:
        form = EventForm()

    context = {
        'form': form,
        'is_create': True,
    }
    return render(request, 'pages/events/form.html', context=context)


@login_required
@permission_required("events.change_event", raise_exception=True)
def edit_event(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('list-events')
    else:
        form = EventForm(instance=event)

    context = {
        'form': form,
        'event': event,
        'is_edit': True,
    }
    return render(request, 'pages/events/form.html', context=context)


@login_required
@permission_required("events.delete_event", raise_exception=True)
def delete_event(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == 'POST':
        event.delete()
        return redirect('list-events')

    context = {
        'event': event,
        'is_delete': True,
    }
    return render(request, 'pages/events/form.html', context=context)


@login_required
@permission_required("events.view_event", raise_exception=True)
def detail_event(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'pages/events/detail.html', {'event': event})
