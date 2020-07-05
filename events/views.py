from custom_views.views import PersonalizedListCreateAPIView, PersonalizedRetrieveUpdateDestroyAPIView
from events.models import Event, EventTag
from events.serializers import EventSerializer, EventTagSerializer


class EventListCreateAPIView(PersonalizedListCreateAPIView):
    """ Получение списка событий (GET) и создание новых событий (POST) """
    model = Event
    serializer_class = EventSerializer


class EventDetailAPIView(PersonalizedRetrieveUpdateDestroyAPIView):
    """ Детальная информация о событии, редактирование и удаление """
    serializer_class = EventSerializer
    read_serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventTagListCreateAPIView(PersonalizedListCreateAPIView):
    """ Получение списка тегов (GET) и создание новых тегов (POST) """
    model = EventTag
    serializer_class = EventTagSerializer
