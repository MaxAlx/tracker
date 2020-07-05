from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from customizations import views
from events.models import Event, EventTag
from events.serializers import EventSerializer, EventReadSerializer, EventTagSerializer


class EventListCreateAPIView(views.PersonalizedListCreateAPIView):
    """ Получение списка событий (GET) и создание новых событий (POST) """
    model = Event
    serializer_class = EventSerializer
    read_serializer_class = EventReadSerializer


class EventDetailAPIView(views.PersonalizedRetrieveUpdateDestroyAPIView):
    """ Детальная информация о событии, редактирование и удаление """
    serializer_class = EventSerializer
    read_serializer_class = EventReadSerializer
    queryset = Event.objects.all()


class EventTagListCreateAPIView(ListCreateAPIView):
    """ Получение списка тегов (GET) и создание новых тегов (POST) """
    permission_classes = [IsAuthenticated]
    serializer_class = EventTagSerializer
    queryset = EventTag.objects.all()


class EventListByDateAPIView(views.ListByDateAPIView):
    """ Получение событий за определённый день """
    model = Event
    serializer_class = EventReadSerializer
    queryset = Event.objects.all()
