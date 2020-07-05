from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import NotAcceptable


class CustomListCreateAPIView(ListCreateAPIView):
    """ Персонализированный ListCreateAPIView (по дефолту поля заполняюся авторизованным пользователем) """
    model = None

    def get_queryset(self):
        """ Список сущностей только авторизованного пользователя """
        return self.model.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """ Заполняем поле user текущим пользователем """
        serializer.save(user=self.request.user)


class CustomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    read_serializer_class = None

    def get_serializer_class(self, *args, **kwargs):
        """ Если требуется, для GET-запосов используем другой serializer """
        if self.read_serializer_class and self.request.method == 'GET':
            return self.read_serializer_class

        return self.serializer_class

    def get_queryset(self):
        """ Только вледелец сущности сможет ее получить """
        return super(CustomRetrieveUpdateDestroyAPIView, self).get_queryset().filter(user=self.request.user)


class CustomScheduleAPIView(RetrieveUpdateAPIView):
    """
    Получение информации о расписании на неделю, редактирование и удаление
    c проверкой на принадлежность расписаний авторизованному пользователю
    """
    def get_object(self):
        return self.request.user.schedule

    def perform_update(self, serializer):
        if not self.is_day_schedules_owned_by_user(serializer.validated_data):
            raise NotAcceptable
        serializer.save()

    def is_day_schedules_owned_by_user(self, data):
        """ Проверяется все ли запрашиваемые расписания принадлежат этому пользователю """
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        for day in days:
            if data[day] and data[day].user != self.request.user:
                return False

        return True
