from django.db import models


class Playlist(models.Model):
    user = models.OneToOneField('service_auth.CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    link = models.TextField(max_length=200, verbose_name='Ссылка на плейлист или видео')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Плейлист'
        verbose_name_plural = 'Плейлисты'
