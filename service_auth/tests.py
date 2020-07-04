from django.test import TestCase
from service_auth.models import CustomUser


class SchedulesTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(username='Sam', password='123')
        CustomUser.objects.create(username='Harry', password='123')

    def test_additional_created(self):
        """ Проверяется созданы ли дополнительные OneToOne сущности пользователя """
        for username in ['Sam', 'Harry']:
            user = CustomUser.objects.get(username=username)
            self.assertEqual(user.usersschedule.user.username, username)  # schedules.models.UsersSchedule
            self.assertEqual(user.note.user.username, username)  # notes.models.Note
            self.assertEqual(user.playlist.user.username, username)  # playlists.models.Playlist
