from django.contrib import admin
from schedules.models import UsersSchedule, Schedule, Task


@admin.register(UsersSchedule)
class UsersScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    filter_horizontal = ('tasks',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
