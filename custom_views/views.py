from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class PersonalizedListCreateAPIView(ListCreateAPIView):
    """
    Персонализированный ListCreateAPIView.
    По дефолту поля `user` заполняюся авторизованным пользователем
    """
    permission_classes = [IsAuthenticated]
    model = None

    def get_queryset(self):
        """ Список сущностей только авторизованного пользователя """
        return self.model.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """ Заполняем поле user текущим пользователем """
        serializer.save(user=self.request.user)


class PersonalizedRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Персонализированный RetrieveUpdateDestroyAPIView.
    Пользователи могут взимодействовать только с теми объектами, которыми они владеют.
    Можно использовать альтернативный serializer для GET-запросов
    """
    permission_classes = [IsAuthenticated]
    read_serializer_class = None

    def get_serializer_class(self, *args, **kwargs):
        """ Если требуется, для GET-запосов используем другой serializer """
        if self.read_serializer_class and self.request.method == 'GET':
            return self.read_serializer_class

        return self.serializer_class

    def get_queryset(self):
        """ Только вледелец сущности сможет ее получить """
        return super(PersonalizedRetrieveUpdateDestroyAPIView, self).get_queryset().filter(user=self.request.user)