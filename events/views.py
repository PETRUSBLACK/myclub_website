from django.shortcuts import render
from datetime import datetime
import calendar
from calendar import HTMLCalendar
now = datetime.now()


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
 