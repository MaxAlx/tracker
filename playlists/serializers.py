from rest_framework import serializers
from playlists.models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        exclude = ['user']
