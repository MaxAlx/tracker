from django.db import models


class Schedule(models.Model):
    """ Модель расписания дня """
    user = models.OneToOneField('serv_auth.CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    days = models.ManyToManyField('schedules.WeekDay', blank=True, related_name='weekdaysAsDays', verbose_name='Дни')
    tasks = models.ManyToManyField('schedules.Task', blank=True, related_name='weekendsAsTask', verbose_name='Задачи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class Task(models.Model):
    """ Задачи в течение дня """
    user = models.ForeignKey('serv_auth.CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    datetime = models.TimeField(verbose_name='Время события')
    description = models.TextField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class WeekDay(models.Model):
    """ Дни недели """
    name = models.CharField(max_length=10, verbose_name='Название')
    NAMES_CHOICES = (
        (0, 'пн'),
        (1, 'вт'),
        (2, 'ср'),
        (3, 'чт'),
        (4, 'пт'),
        (5, 'сб'),
        (6, 'вс')
    )
    short_name = models.IntegerField(choices=NAMES_CHOICES, verbose_name='Краткие названия')
    number = models.IntegerField(verbose_name='Номер дня недели')

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'
