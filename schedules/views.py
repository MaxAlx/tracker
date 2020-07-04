from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from schedules.models import Task
from schedules.serializers import TaskSerializer


class TaskListCreateAPIView(ListCreateAPIView):
    """ Создание новых задач (POST) и получение списка задач (GET) / информации по заполнению (OPTIONS) """
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        """ Список задач авторизованного пользователя """
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """ Заполняем поле user текущим пользователем """
        serializer.save(user=self.request.user)


class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ Получение информации о задаче, редактирование и удаление """
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        """ Только вледелец задачи сможет ее получить """
        return super(TaskRetrieveUpdateDestroyAPIView, self).get_queryset().filter(user=self.request.user)
