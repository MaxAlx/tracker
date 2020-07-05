from schedules.services.custom_views import CustomListCreateAPIView, CustomRetrieveUpdateDestroyAPIView, CustomScheduleAPIView
from rest_framework.permissions import IsAuthenticated
from schedules.models import Task, DaySchedule, Schedule
from schedules import serializers


class TaskListCreateAPIView(CustomListCreateAPIView):
    """ Создание новых задач (POST) и получение списка задач (GET) """
    model = Task
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveUpdateDestroyAPIView(CustomRetrieveUpdateDestroyAPIView):
    """ Получение информации о задаче, редактирование и удаление """
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()


class DayScheduleListCreateAPIView(CustomListCreateAPIView):
    """ Создание расписаний на день (POST) и получение списка (GET) """
    model = DaySchedule
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.DayScheduleSerializer
    queryset = DaySchedule.objects.all()


class DayScheduleRetrieveUpdateDestroyAPIView(CustomRetrieveUpdateDestroyAPIView):
    """ Получение информации о расписании на день, редактирование и удаление """
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.DayScheduleSerializer
    read_serializer_class = serializers.DayScheduleReadSerializer
    queryset = DaySchedule.objects.all()


class ScheduleRetrieveUpdateAPIView(CustomScheduleAPIView):
    """ Получение информации о расписании на неделю, редактирование и удаление """
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ScheduleSerializer
    queryset = Schedule.objects.all()
