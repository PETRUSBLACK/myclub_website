from django.contrib import admin
from .models import Event, Venue, MyClubUser

# Register your models here.
admin.site.register((Event, Venue, MyClubUser))
