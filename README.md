## Описание.
Обучающий сайт "Food Academy".

Layout:
```
app/ - проект
    manage.py
    config/
        settings/
            base.py - общие настройки
            dev.py  - настройки development
            prod.py - настройки production
        urls.py - настройки URL
        wsgi.py - настройки WSGI
    contactus/  - приложение для обратной связи
        migrations/ 
        tests/    
        admin.py
        apps.py
        models.py
        urls.py
    courses/    - основное приложение (курсы, группы, расписание)
        migrations/ 
        tests/     
        admin.py
        app.py
        models.py
        urls.py
    users/  - приложение для управления пользоваталями (администраторы, преподаватели, студенты)
        migrations/ 
        tests/     
        admin.py
        app.py
        managers.py
        models.py
        urls.py
deploy/ - вспомогательные файлы для развёртывания проекта.
```

### Установка и запуск (пример для Linux).
```
# mkdir FoodAcademy
# cd FoodAcademy/
# git clone https://github.com/nikitasellin/FoodAcademy.git .
```
**Важно! В целях безопасности, рекомендуется сменить секретный ключ и реквизиты доступа к БД в
файлах .env и config/dev.py**

Запуск.
```
# docker-compose up [-d]
```
После успешного запуска, интерфейс доступен по адресу:
```
http://127.0.0.1:8000/ (стартовая страница Django)
```
Для авторизации используется custom-модель (авторизация по уникальному e-mail). 
Для доступа к администрированию, необходимо создать super-пользователя:
```
# docker-compose exec app ./manage.py createsuperuser
```
указать e-mail, пароль и затем авторизоваться с этими данными:
```
http://127.0.0.1:8000/admin/ (Администрирование Django)
```

