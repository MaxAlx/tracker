from rest_framework import serializers
from schedules.models import Task, DaySchedule, Schedule


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['user']


class DayScheduleSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = DaySchedule
        exclude = ['user']


class DayScheduleReadSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(read_only=True, many=True)

    class Meta:
        model = DaySchedule
        exclude = ['user']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleReadSerializer(ScheduleSerializer):
    monday = DayScheduleReadSerializer(read_only=True)
    tuesday = DayScheduleReadSerializer(read_only=True)
    wednesday = DayScheduleReadSerializer(read_only=True)
    thursday = DayScheduleReadSerializer(read_only=True)
    friday = DayScheduleReadSerializer(read_only=True)
    saturday = DayScheduleReadSerializer(read_only=True)
    sunday = DayScheduleReadSerializer(read_only=True)
