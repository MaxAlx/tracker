from django.db import models


class Event(models.Model):
    user = models.ForeignKey('service_auth.CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    date = models.DateField(verbose_name='Дата события')
    time = models.TimeField(verbose_name='Время события')
    tags = models.ManyToManyField('events.EventTag', blank=True, verbose_name='Теги')
    description = models.TextField(max_length=255, blank=True, verbose_name='Описание')

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
