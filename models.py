from django.db import models

from datetime import datetime
from django.forms import ModelForm 



class EventCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EventAgenda(models.Model):
    title = models.CharField(max_length=100)
    # description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(default=datetime(2023, 12, 31, 23, 59, 59))

    def __str__(self):
        return self.title

class EventMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()  # Make sure the email field is defined like this
    phone = models.CharField(max_length=20, blank=True, null=True)
    job_category = models.ForeignKey('EventJobCategoryLinking', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

class EventJobCategoryLinking(models.Model):
    name = models.CharField(max_length=100)
    status_choices = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('blocked', 'Blocked'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True, blank=True)
    agendas = models.ManyToManyField(EventAgenda, blank=True)
    members = models.ManyToManyField(EventMember, blank=True)

    def __str__(self):
        return self.title


    
class EventAgendaForm(ModelForm):
    class Meta:
        model = EventAgenda
        fields = '__all__'
        
     

