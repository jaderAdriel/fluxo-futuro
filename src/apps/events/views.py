from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm

def index(request):
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
    return render(request, 'pages/events/create.html', {'form': form})

def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('list-events')
    else:
        form = EventForm(instance=event)
    return render(request, 'pages/events/edit.html', {'form': form, 'event': event})

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('list-events')
    return render(request, 'pages/events/delete.html', {'event': event})

