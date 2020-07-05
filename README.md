![Banner](https://github.com/MaxAlx/tracker/blob/master/Banner.jpg)

# Tracker

## Описание приложения

Tracker - это веб-приложение, с помощью которого можно легко следовать запланированному графику дня. Приложение состоит из нескольких основных частей: расписание на день (можно составить несколько расписаний и прявязать их к разным дням недели), нерегулярные события, которые важно трекать, плейлист (YouTube-плеер) и заметки.

Back-end приложения написан на Django, БД - PostgreSQL. 

## Документация по REST API

С back-end приложения можно взаимодействовать по REST API (использовался Django Rest Framework). Ниже будут описаны методы REST API.  

### Авторизация

Авторизация реализована через Google OAuth2. Пользователи могут авторизоваться под Google-аккаунтом и взаимодействовать с сервисом через JWT.

Получение JWT:
```http request
POST /auth/google/
{
    "access_token": "ya.fese3srg4tsf..."
}
```

При последующих запросах на сервис необходимо передавать полученный токен в HTTP-заголовках:
```http request
Authorization: Token eyJ0eXAiOiJKV...
```

**Важно**: все запросы, описанные ниже, требуют авторизации.

### Расписание на неделю

Приложение, отвечающее за расписание состоит из следующих частей:
1. Задачи
2. Расписание не день (состоит из задач)
3. Расписание на неделю (сопоставление "День недели" > "Расписание не день")

Получение списка задач пользователя:
```http request
GET /api/v1/schedules/tasks/
```

Создание новой задачи:
```http request
POST /api/v1/schedules/tasks/
{
    "title": "Поработать на проектом",
    "date": "2020-07-15",
    "time": "11:00",
    "description": "В течении двух часов не отвлекаться на другие дела"
}
```

Подробная информация о задача по её ID:
```http request
GET /api/v1/schedules/tasks/12/
```

Редактирование задачи:
```http request
PUT /api/v1/schedules/tasks/12/
{
    "title": "Поработать на проектом",
    "date": "2020-07-15",
    "time": "11:30",
    "description": "В течении хотя бы одного часа не отвлекаться на другие дела"
}
```

Удаление задачи:
```http request
DELETE /api/v1/schedules/tasks/12/
```

Получение списка расписаний на день пользователя:
```http request
GET /api/v1/schedules/
```

Создание нового расписания на день:
```http request
POST /api/v1/schedules/
{
    "title": "Продуктивный день",
    "tasks": [3, 8, 12]
}
```

Подробная информация о расписании по его ID:
```http request
GET /api/v1/schedules/12/
```

Редактирование расписания:
```http request
PUT /api/v1/schedules/12/
{
    "title": "Продуктивный день",
    "tasks": [3, 8, 9, 12, 15]
}
```

Удаление расписания на день:
```http request
DELETE /api/v1/schedules/12/
```

Получение расписания на неделю:

```http request
GET /api/v1/schedules/common/
```

Редактирование расписания на неделю (передаются ID расписаний на день):
```http request
PUT /api/v1/schedules/common/
{
    "monday": 4,
    "tuesday": null,
    "wednesday": null,
    "thursday": null,
    "friday": 3,
    "saturday": null,
    "sunday": null
}
```

Сброс расписания на неделю (значения для каждого дня становится null)
```http request
POST /api/v1/schedules/common/reset/
```


### События

Приложение, отвечающее за события состоит из двух моделей:
1. Событие
2. Тег события

Получение списка событий пользователя:
```http request
GET /api/v1/events/
```

Получение списка событий пользователя за определённую дату:
```http request
GET /api/v1/events/2020-07-23/
```

Создание нового события:
```http request
POST /api/v1/events/
{
    "title": "Event 1",
    "date": "2020-07-23",
    "time": "20:00",
    "tags": [2, 3]
}
```

Подробная информация о событии:
```http request
GET /api/v1/events/34/
```

Редактирование события:
```http request
PUT /api/v1/events/34/
{
    "title": "Event 1",
    "date": "2020-07-24",
    "time": "15:30",
    "tags": []
}
```

Удаление события:
```http request
DELETE /api/v1/events/34/
```

Получение списка тегов событий:
```http request
GET /api/v1/events/tags/
```

Создание нового тега событий:
```http request
POST /api/v1/events/tags/
{
    "title": "Обучение"
}
```


### Плейлист

Получение текущего плейлиста пользователей:
```http request
GET /api/v1/playlist/
```

Изменить плейлист пользователей:
```http request
PUT /api/v1/playlist/
{
"link": "<iframe width="560" height="315" src="https://www.youtube.com/embed/UOUBW8bkjQ4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"
}
```

### Заметки

Получение пользовательской заметки:
```http request
GET /api/v1/note/
```

Редактирование пользовательской заметки:
```http request
PUT /api/v1/note/
{
    "text": "Сделать что-нибудь"
}
```
