from rest_framework import serializers
from events.models import Event, EventTag


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['user']


class EventTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTag
        fields = '__all__'
