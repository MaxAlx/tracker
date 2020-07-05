from rest_framework import serializers
from events.models import Event, EventTag


class EventTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTag
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['user']


class EventReadSerializer(EventSerializer):
    tags = EventTagSerializer(read_only=True, many=True)
