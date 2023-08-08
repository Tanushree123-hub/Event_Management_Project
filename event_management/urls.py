from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
]

urlpatterns = [
    path('temporary/', views.temporary_view, name='temporary_view'),
]

urlpatterns = [
    path('Event-Agenda/', views.event_agenda_list, name='event_agenda_list'),
    path('Event-Member/', views.event_member_list, name='event_member_list'),
    path('Event-Job-Category/', views.event_job_category_list, name='event_job_category_list'),
    path('create-Event-Agenda/', views.create_event_agenda, name='create_event_agenda'),
]