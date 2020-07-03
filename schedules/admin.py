from django.contrib import admin
from schedules.models import Schedule, Task, WeekDay


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    filter_horizontal = ('days', 'tasks')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')


@admin.register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'number')
