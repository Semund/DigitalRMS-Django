# Digital RMS

Проект Web-портала для управления номером в отеле во время проживания. Планируемый основной функционал проекта:
* Авторизация гостя на портале по паспортным данным;
* Чат гостя с администратором отеля;
* Управление системами (освещение и климат) в номере;
* Заказ еды в номер.

## Описание

Проект реализован на базе 2 Django + DRF - проектов:

* `hotel` - Сервер для имитации работы систем отеля;
* `webportal` - Сервер для Web-портала.

### Сервер Hotel

На данный момент реализован следующий функционал:

1) `hotel/registration` - сервис имитации регистрации/заселения гостя в отеле. Реализован функционал:
    * Добавления данных гостя и проживания в БД при заполнении форм на странице заселения;
    * API для валидации данных гостя при аутентификации на Web-портале.


2) `hotel/room_automation` - сервис имитации контроля автоматизации систем номера. Реализован функционал:
    * API для CRUD операций с БД со стороны Web-портала;
    * WebSocket-соединение между web-страницей и сервером для отображения работы систем номера при их изменении без 
      обновления страницы.


3) `hotel/restaurant` - сервис имитации работы ресторана. В разработке.

### Сервер Webportal

На данный момент реализованы следующий функционал:

1) `webportal/main` - сервис главной страницы портала. Реализован функционал:
    * Созданы `management/commands` для сбора данных о прогнозе погоды и ближайших мероприятий , запись этих данных в БД и добавление на главную страницу Web-портала.


2) `webportal/authorization` - сервис авторизации гостя на портале. Реализован функционал:
    * Создана custom-модель User и custom-backend для аутентификации без пароля;
    * Перед аутентификацией данные гостя проверяются на стороне сервера `hotel` через API `hotel/registration`


3) `webportal/room_control` - сервис управления светом и климатом в номере. Реализован функционал:
    * Сигналы управления системами отправляются на API `hotel/room_automation` без участия сервера с помощью функций JS `fetch` и `XMLHttpRequest`;


## Установка

1) Скопируйте проект и перейдите в папку DigitalRMS:

```
git clone https://github.com/Semund/DigitalRMS.git
cd ./DigitalRMS
```

2) Установите необходимые python библиотеки:
```
pip install -r ./requirements.txt
```

3) Скопировать файлы локальных настроек серверов:
```
cp ./hotel/hotel/settings_local.py.default ./hotel/hotel/settings_local.py
cp ./webportal/webportal/settings_local.py.default ./webportal/webportal/settings_local.py
```

4) Для работы сервера `hotel` необходимо ввести свои параметры в файле `hotel/hotel/settings_local.py`:
   * `PSQL_NAME_DB, PSQL_USER, PSQL_PASSWORD, PSQL_HOST, PSQL_PORT` данные подключения к PostgreSQL сервера `hotel`;  
   * `REDIS_HOST, REDIS_PORT` данные подключения к базе данных Redis.


5) Для работы сервера `webportal` необходимо ввести свои параметры в файле `webportal/webportal/settings_local.py`:
   * `PSQL_NAME_DB, PSQL_USER, PSQL_PASSWORD, PSQL_HOST, PSQL_PORT` данные подключения к PostgreSQL сервера `webportal`;
   * `WEATHER_API_KEY` для доступа к данным погоды от [сервиса прогноза погоды](https://api.openweathermap.org) (https://api.openweathermap.org);
   * `EVENTS_PLACE` Указать город, мероприятия которого необходимо получить. 


6) Создать таблицы баз данных, выполнив миграции:
```
python hotel/manage.py migrate
python webportal/manage.py migrate
```

7) Собрать данные о погоде и мероприятиях:
```
python webportal/manage.py get_weather
python webportal/manage.py get_events -d "in YYYY-MM-DD format" -n "Num days (int)"
```

8) Запустить сервер `hotel`:
```
python hotel/manage.py runserver 8001
```

9) Запустить сервер `webportal`:
```
python webportal/manage.py runserver
```