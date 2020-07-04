from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CustomListCreateAPIView(ListCreateAPIView):
    model = None

    def get_queryset(self):
        """ Список сущностей только авторизованного пользователя """
        return self.model.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """ Заполняем поле user текущим пользователем """
        serializer.save(user=self.request.user)


class CustomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    read_serializer_class = None

    def get_serializer_class(self, *args, **kwargs):
        """ Если требуется, для GET-запосов используем другой serializer """
        if self.read_serializer_class:
            if self.request.method == 'GET':
                return self.read_serializer_class

        return self.serializer_class

    def get_queryset(self):
        """ Только вледелец сущности сможет ее получить """
        return super(CustomRetrieveUpdateDestroyAPIView, self).get_queryset().filter(user=self.request.user)
