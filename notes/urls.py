from django.urls import path
from notes.views import NoteRetrieveUpdateAPIView


# /api/v1/note/
urlpatterns = [
    path('', NoteRetrieveUpdateAPIView.as_view())
]
