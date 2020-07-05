from django.contrib import admin
from events.models import Event, EventTag


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'date', 'time')
    filter_horizontal = ('tags',)


@admin.register(EventTag)
class EventTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
