from schedules.services.custom_views import CustomScheduleAPIView, CustomScheduleResetAPIView
from customizations.views import PersonalizedListCreateAPIView, PersonalizedRetrieveUpdateDestroyAPIView
from schedules.models import Task, DaySchedule, Schedule
from schedules import serializers


class TaskListCreateAPIView(PersonalizedListCreateAPIView):
    """ Создание новых задач (POST) и получение списка задач (GET) """
    model = Task
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveUpdateDestroyAPIView(PersonalizedRetrieveUpdateDestroyAPIView):
    """ Получение информации о задаче, редактирование и удаление """
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()


class DayScheduleListCreateAPIView(PersonalizedListCreateAPIView):
    """ Создание расписаний на день (POST) и получение списка (GET) """
    model = DaySchedule
    serializer_class = serializers.DayScheduleSerializer
    queryset = DaySchedule.objects.all()


class DayScheduleRetrieveUpdateDestroyAPIView(PersonalizedRetrieveUpdateDestroyAPIView):
    """ Получение информации о расписании на день, редактирование и удаление """
    serializer_class = serializers.DayScheduleSerializer
    read_serializer_class = serializers.DayScheduleReadSerializer
    queryset = DaySchedule.objects.all()


class ScheduleRetrieveUpdateAPIView(CustomScheduleAPIView):
    """ Получение информации о расписании на неделю, редактирование и удаление """
    serializer_class = serializers.ScheduleSerializer
    read_serializer_class=serializers.ScheduleReadSerializer
    queryset = Schedule.objects.all()


class ScheduleResetAPIView(CustomScheduleResetAPIView):
    """ Сбросить расписание на неделю (очистить дни недели) """
    model = Schedule
