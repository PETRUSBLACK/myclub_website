from django.shortcuts import render
from datetime import datetime
import calendar
from django.http import HttpResponseRedirect
from calendar import HTMLCalendar

from .models import Event
from .forms import VenueForm 
now = datetime.now()

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
 