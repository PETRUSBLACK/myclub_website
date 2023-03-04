from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events/',  views.all_events,  name = "list-events"),
    path('add_venue', views.add_venue, name='add-venue'),
    path('list_venues', views.list_venues, name='list-venues'),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('Search_venus', views.Search_venus, name='Search-venus'),
    # path('update_venue/<venue_id>', views.Update_venue, name='update-venue'),
    # path('update_event/<venue_id>', views.Update_event, name='update-event'),
    path('add_event', views.add_event, name='add-event'),




]