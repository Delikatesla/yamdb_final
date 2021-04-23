<!---
https://github.com/AlexanderNkn/yamdb_final/workflows/yamdbworkflow/badge.svg
--->
![yamdb%20workflow Actions Status](https://github.com/delikatesla/yamdb_final/workflows/yamdb%20workflow/badge.svg)
[![api_yamdb workflow](https://github.com/Delikatesla/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg?branch=master)](https://github.com/Delikatesla/yamdb_final/actions/workflows/yamdb_workflow.yaml)

# **YAMDB**
**REST API для сервиса YaMDB** — базы данных о фильмах, книгах и музыке.
***
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Компьютерные игры»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы (Review) и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок автоматически высчитывается средняя оценка произведения.
***
## **Описание API**
**API для сервиса YaMDb. Позволяет работать со следующими сущностями:**
- **Отзывы:**
  + получить список всех отзывов;
  + создать новый отзыв;
  + получить отзыв по id;
  + частично обновить отзыв по id;
  + удалить отзыв по id.
- **Комментарии к отзывам:**
  + Получить список всех комментариев к отзыву по id;
  + создать новый комментарий для отзыва, получить комментарий для отзыва по id;
  + частично обновить комментарий к отзыву по id;
  + удалить комментарий к отзыву по id.
- **JWT-токен:**
  + Отправление confirmation_code на переданный email;
  + получение JWT-токена в обмен на email и confirmation_code.
- **Пользователи:**
  + Получить список всех пользователей;
  + создание пользователя получить пользователя по username;
  + изменить данные пользователя по username;
  + удалить пользователя по username;
  + получить данные своей учетной записи;
  + изменить данные своей учетной записи.
- **Категории (типы) произведений:**
  + Получить список всех категорий;
  + создать категорию;
  + удалить категорию.
- **Категории жанров:**
  + получить список всех жанров
  + создать жанр;
  + удалить жанр.
- **Произведения, к которым пишут отзывы:**
  + Получить список всех объектов;
  + создать произведение для отзывов;
  + информация об объекте;
  + обновить информацию об объекте;
  + удалить произведение.
***
## **Алгоритм регистрации пользователей**
1. Пользователь отправляет запрос с параметром email на `/auth/email/`.
2. YaMDB отправляет письмо с кодом подтверждения `(confirmation_code)` на адрес `email`.
3. Пользователь отправляет запрос с параметрами `email` и `confirmation_code` на `/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на `/users/me/` и заполняет поля в своём профайле (описание полей — в документации).
***
## **Пользовательские роли**
- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
- **Аутентифицированный пользователь** — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить рейтинг произведениям (фильмам/книгам/песням), может комментировать чужие отзывы и ставить им оценки; может редактировать и удалять свои отзывы и комментарии.
- **Модератор** — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
- **Администратор** — полные права на управление проектом и всем его содержимым. Может создавать и удалять категории и произведения. Может назначать роли пользователям.
***
## **Доступные методы:**

### Reviews

`/api/v1/titles/{title_id}/reviews/ (GET, POST)`

`/api/v1/titles/{title_id}/reviews/{review_id}/ (GET, PATCH, DELETE)`

### Comments

`/api/v1/titles/{title_id}/reviews/{review_id}/comments/ (GET, POST)`

`/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ (GET PATCH, DELETE)`

### Auth

`/api/v1/auth/token/ (POST)`

`/api/v1/auth/email/ (POST)`

### Users 

`/api/v1/users/ (GET, POST)`

`/api/v1/users/{username}/ (GET, PATCH, DELETE)`

`/api/v1/users/me/ (GET, PATCH)`

### Categories

`/api/v1/categories/ (GET, POST)`

`/api/v1/categories/{slug}/ (DELETE)`

### Genres

`/api/v1/genres/ (GET, POST)`

`/api/v1/genres/{slug}/ (DELETE)`

### Titles

`/api/v1/titles/ (GET, POST)`

`/api/v1/titles/{titles_id}/ (GET, PATCH, DELETE)`

***
## Запуск проекта локально  
1. Запустить docker-compose:

`docker-compose up`

2. При первом запуске для функционирования проекта обязательно создать и выполнить миграции:

`docker-compose exec web python manage.py makemigrations`
`docker-compose exec web python manage.py migrate`

3. Чтобы загрузить записи в БД:

`docker-compose exec web python manage.py loaddata fixtures.json`

4. Для создания суперпользователя введите следующую команду:

`docker-compose exec web python manage.py createsuperuser`

5. Соберите статику командой:

`docker-compose exec web python manage.py collectstatic`

## Деплой на удаленный сервер
Для запуска проекта на удаленном сервере необходимо:
- скопировать на сервер файлы `docker-compose.yaml`, `.env` и папку `nginx` командами:
```
scp docker-compose.yaml  <user>@<server-ip>:
scp .env <user>@<server-ip>:
scp -r nginx/ <user>@<server-ip>:

```
- создать переменные окружения в разделе `secrets` настроек текущего репозитория:
```
DOCKER_PASSWORD # Пароль от Docker Hub
DOCKER_USERNAME # Логин от Docker Hub
HOST # Публичный ip адрес сервера
USER # Пользователь зарегистрированный на сервере
PASSPHRASE # Если ssh-ключ защищен фразой-паролем
SSH_KEY # Приватный ssh-ключ
TELEGRAM_TO # ID телеграм-аккаунта
TELEGRAM_TOKEN # Токен бота
```

### После каждого обновления репозитория (`git push`) будет происходить:
1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest из репозитория yamdb_final
2. Сборка и доставка докер-образов на Docker Hub.
3. Автоматический деплой.
4. Отправка уведомления в Telegram.

***
## **Технологии**
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [DRF Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
***
## **Участники**
- [timrock23](https://github.com/TimRock23) - управление пользователями (Auth и Users):
  + система регистрации и аутентификации;
  + права доступа, работа с токеном;
  + система подтверждения e-mail, поля.
- [delikatesla](https://github.com/Delikatesla) - категории (Categories), жанры (Genres) и произведения (Titles):
  + модели и view;
  + эндпойнты;
  + докеризация, CI.
- [lenprofy](https://github.com/lenprofy) - отзывы (Review) и комментарии (Comments):
  + модели и view;
  + эндпойнты;
  + права доступа для запросов;
  + рейтинги произведений.
  
***