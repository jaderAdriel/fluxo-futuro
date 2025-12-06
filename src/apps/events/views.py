from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm


def list_events(request):
    events = Event.objects.all()
    return render(request, 'pages/events/index.html', {'events': events})


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

def detail_event(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'pages/events/detail.html', {'event': event})
