from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from playlists.serializers import PlaylistSerializer


class PlaylistRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlaylistSerializer

    def get_object(self):
        return self.request.user.playlist
