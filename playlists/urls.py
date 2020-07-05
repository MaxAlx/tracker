from django.urls import path
from playlists.views import PlaylistRetrieveUpdateAPIView


# /api/v1/playlist/
urlpatterns = [
    path('', PlaylistRetrieveUpdateAPIView.as_view())
]
