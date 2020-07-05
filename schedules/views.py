from schedules.services import custom_views
from schedules.models import Task, DaySchedule, Schedule
from schedules import serializers


class TaskListCreateAPIView(custom_views.CustomListCreateAPIView):
    """ Создание новых задач (POST) и получение списка задач (GET) """
    model = Task
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveUpdateDestroyAPIView(custom_views.CustomRetrieveUpdateDestroyAPIView):
    """ Получение информации о задаче, редактирование и удаление """
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()


class DayScheduleListCreateAPIView(custom_views.CustomListCreateAPIView):
    """ Создание расписаний на день (POST) и получение списка (GET) """
    model = DaySchedule
    serializer_class = serializers.DayScheduleSerializer
    queryset = DaySchedule.objects.all()


class DayScheduleRetrieveUpdateDestroyAPIView(custom_views.CustomRetrieveUpdateDestroyAPIView):
    """ Получение информации о расписании на день, редактирование и удаление """
    serializer_class = serializers.DayScheduleSerializer
    read_serializer_class = serializers.DayScheduleReadSerializer
    queryset = DaySchedule.objects.all()


class ScheduleRetrieveUpdateAPIView(custom_views.CustomScheduleAPIView):
    """ Получение информации о расписании на неделю, редактирование и удаление """
    serializer_class = serializers.ScheduleSerializer
    queryset = Schedule.objects.all()


class ScheduleResetAPIView(custom_views.CustomScheduleResetAPIView):
    """ Сбросить расписание на неделю (очистить дни недели) """
    model = Schedule
