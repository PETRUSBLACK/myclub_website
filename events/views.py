from django.shortcuts import render
from datetime import datetime
import calendar
from calendar import HTMLCalendar

def home(request, year, month):
    month = month.capitalize()

    # Converting month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create a calendar
    cal = HTMLCalendar().formatmonth(
        year, 
        month_number)

    # creating a current time
    now = datetime.now()
    time = now.strftime('%I:%M %p')
    return render(request, "home.html", {
        "month": month,
        "month_number" : month_number,
        "cal" : cal,
        "time" : time
    })
 