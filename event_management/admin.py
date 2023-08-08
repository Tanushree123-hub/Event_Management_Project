from django.contrib import admin

from .models import Event,EventAgenda, EventMember, EventJobCategoryLinking

# Register your models here
admin.site.register(EventAgenda)
admin.site.register(EventMember)
admin.site.register(EventJobCategoryLinking)
admin.site.register(Event)

class EventAgendaAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_time', 'end_time']
    search_fields = ['title']

class EventMemberAdmin(admin.ModelAdmin):
     list_display = ['name', 'email', 'phone']
     list_filter = ['job_category']

class EventJobCategoryLinkingAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')  # Display these fields in the list view
    list_filter = ('start_date', 'end_date')           # Add filters for these fields in the right sidebar
    search_fields = ('title', 'description')           # Enable search by these fields