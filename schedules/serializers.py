from rest_framework import serializers
from schedules.models import Task, DaySchedule


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
