from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response
from rest_framework import status
from schedules.serializers import ScheduleSerializer


class CustomListCreateAPIView(ListCreateAPIView):
    """
    Персонализированный ListCreateAPIView
    (по дефолту поля заполняюся авторизованным пользователем)
    """
    permission_classes = [IsAuthenticated]
    model = None

    def get_queryset(self):
        """ Список сущностей только авторизованного пользователя """
        return self.model.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """ Заполняем поле user текущим пользователем """
        serializer.save(user=self.request.user)


class CustomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]

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


class CustomScheduleResetAPIView(APIView):
    """ Сбросывается расписание на неделю """
    permission_classes = [IsAuthenticated]
    model = None

    def post(self, request):
        try:
            serialized_schedule = self.reset_schedule(request.user.schedule)
            return Response(serialized_schedule, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def reset_schedule(self, schedule):
        schedule.monday = None
        schedule.tuesday = None
        schedule.wednesday = None
        schedule.thursday = None
        schedule.friday = None
        schedule.saturday = None
        schedule.sunday = None
        schedule.save()
        return ScheduleSerializer(schedule).data
