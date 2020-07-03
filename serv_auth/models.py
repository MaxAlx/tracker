from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from schedules.models import UsersSchedule


class CustomUser(AbstractUser):
    pass


@receiver(post_save, sender=CustomUser)
def create_connected_models(sender, instance, created, **kwargs):
    """ Метод создаёт дополнительные сущности при создании нового пользователя """
    if created:
        UsersSchedule.objects.create(user=instance)
