from django.db import models


class Schedule(models.Model):
    """ Расписание на неделю (создаётся при создании нового пользователя) """
    user = models.OneToOneField('service_auth.CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    monday = models.ForeignKey('schedules.DaySchedule', on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='scheduleAsMonday', verbose_name='Понедельник')
    tuesday = models.ForeignKey('schedules.DaySchedule', on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='scheduleAsTuesday', verbose_name='Вторник')
    wednesday = models.ForeignKey('schedules.DaySchedule', on_delete=models.SET_NULL, blank=True, null=True,
                                  related_name='scheduleAsWednesday', verbose_name='Среда')
    thursday = models.ForeignKey('schedules.DaySchedule', on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='scheduleAsThursday', verbose_name='Четверг')
    friday = models.ForeignKey('schedules.DaySchedule', on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='scheduleAsFriday', verbose_name='Пятница')
    saturday = models.ForeignKey('schedules.DaySchedule', on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='scheduleAsSaturday', verbose_name='Суббота')
    sunday = models.ForeignKey('schedules.DaySchedule', on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='scheduleAsSunday', verbose_name='Воскресение')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Расписание на неделю'
        verbose_name_plural = 'Расписания на неделю'


class DaySchedule(models.Model):
    """ Расписание дня """
    title = models.CharField(max_length=50, verbose_name='Название расписания')
    user = models.ForeignKey('service_auth.CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    tasks = models.ManyToManyField('schedules.Task', blank=True, related_name='weekendsAsTask', verbose_name='Задачи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class Task(models.Model):
    """ Задача в течение дня """
    user = models.ForeignKey('service_auth.CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    date = models.DateField(verbose_name='Дата события')
    time = models.TimeField(verbose_name='Время события')
    description = models.TextField(max_length=150, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
