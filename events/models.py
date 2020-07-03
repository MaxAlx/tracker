from django.db import models


class Event(models.Model):
    user = models.ForeignKey('service_auth.CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    datetime = models.DateTimeField(verbose_name='Дата и время события')
    tags = models.ManyToManyField('events.EventTag', blank=True, verbose_name='Теги')
    description = models.TextField(max_length=255, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class EventTag(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
