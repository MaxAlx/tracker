def is_day_schedules_owned_by_user(user, data):
    """ Проверяется все ли запрашиваемые расписания принадлежат этому пользователю """
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    for day in days:
        if data[day] and data[day].user != user:
            return False

    return True


def clear_schedule(user):
    pass
