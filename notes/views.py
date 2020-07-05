from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from notes.serializers import NoteSerializer


class NoteRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get_object(self):
        return self.request.user.note
