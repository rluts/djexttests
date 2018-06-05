from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from .models import Event

@admin.register(Event)
class EventsAdmin(ForeignKeyAutocompleteAdmin):
    fields = ('name', 'trainer')
    related_search_fields = {
        'trainer': ('about', ),
    }
