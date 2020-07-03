from django.test import TestCase
from service_auth.models import CustomUser


class SchedulesTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(username='Sam', password='123')
        CustomUser.objects.create(username='Harry', password='123')

    def test_users_schedules_created(self):
        """ Проверка созданы ли расписания пользователей """
        user_1 = CustomUser.objects.get(username='Sam')
        user_2 = CustomUser.objects.get(username='Harry')
        self.assertEqual(user_1.usersschedule.user.username, 'Sam')
        self.assertEqual(user_2.usersschedule.user.username, 'Harry')
