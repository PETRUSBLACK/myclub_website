from django.shortcuts import render, redirect
from datetime import datetime
import calendar
from django.http import HttpResponseRedirect
from calendar import HTMLCalendar

from .models import Event, Venue
from .forms import VenueForm, EventForm
now = datetime.now()

def Update_event(request, venue_id):
    event = Event.objects.get(pk=venue_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/update_event.html',  {
        'event' : event,
        'form' : form
    })

def Update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    return render(request, 'events/update_venue.html',  {
        'venue' : venue,
        'form' : form
    })
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html',
    {'form' : form, 'submitted' : submitted})


def Search_venus(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains = searched)
        return render(request, 
        'events/Search_venus.html',
        {'searched': searched,
          'venues': venues })
    else:
        return render(request, 
        'events/Search_venus.html',
        {})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html',  {
        'venue' : venue
    })


def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venue.html',  {
        'venue_list' : venue_list
    })
    

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html',
    {'form' : form, 'submitted' : submitted})

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',  {
        'event_list' : event_list
    })

def home(request, year=now.year, month=now.strftime('%B')):
    name = "Petrus"
    month = month.capitalize()
    year = year

    # Converting month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create a calendar
    cal = HTMLCalendar().formatmonth(
        year, 
        month_number)

    # creating a current time
    time = now.strftime('%I:%M %p')
    return render(request, "events/home.html", {
        "month": month,
        "month_number" : month_number,
        "cal" : cal,
        "time" : time,
        "name" : name,
        "year" : year
    })
 