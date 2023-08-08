from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import EventAgenda, EventMember, EventJobCategoryLinking,EventAgendaForm


from .models import Event


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_management/event_list.html', {'events': events})


def temporary_view(request):
    return HttpResponse("Event Management! This is a temporary view.")

from .models import EventAgenda, EventMember, EventJobCategoryLinking

def event_agenda_list(request):
    agendas = EventAgenda.objects.all()
    return render(request, 'event_management/event_agenda_list.html', {'agendas': agendas})

def event_member_list(request):
    members = EventMember.objects.all()
    return render(request, 'event_management/event_member_list.html', {'members': members})

def event_job_category_list(request):
    job_categories = EventJobCategoryLinking.objects.all()
    return render(request, 'event_management/event_job_category_list.html', {'job_categories': job_categories})


def create_event_agenda(request):
    if request.method == 'POST':
        form = EventAgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_agenda_list')
    else:
        form = EventAgendaForm()

    return render(request, 'event_management/create_event_agenda.html', {'form': form})
