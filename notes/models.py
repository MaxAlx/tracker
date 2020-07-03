from django.db import models


class Note(models.Model):
    user = models.OneToOneField('serv_auth.CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(max_length=255, verbose_name='Текст заметки')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Заметки'
        verbose_name_plural = 'Заметки'
