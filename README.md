# Quests_TelegramBot
Quests_TelegramBot - это бот для Telegram, который помогает отслеживать успешность прививания привычек

### Установка
1. Клонируйте репозиторий, создайте виртуальное окружение
2. Установите зависимости `pip install -r requirements.txt`
3. Получите файл с ключами к сервисам Google, назовите файл credentials.json (<https://habr.com/ru/post/483302/>)
4. Положите файл credentials.json в папку с проектом ```\Quests_TelegramBot```
5. Создайте файл config.py. В тексте укажите информацию формата:
    ```
    TOKEN = "NUMBER_TELEGRAMBOT_TOKEN"
    SPREAD_SHEET_ID = "NUMBER_GOOGLE_SPREAD_SHEET"
   ```
6. Запустите файл ```quest_telegrambot.py```

### Добавление автозапуска бота при старте (Windows)
1. Создайте файл с расширением *.bat 
2. В тексте файла необходимо указать следуйщий текст (первая часть - путь к интерпретатору, вторая часть - путь к скрипту):
    ```C:\_путь к папке проекта_\env\Scripts\python C:\_путь к папке проекта_\Quests_TelegramBot\quest_telegrambot.py```
3. Далее по инструкции <https://www.computerhope.com/issues/ch000322.htm>

### Добавление автозапуска бота при старте (Linux)
1. Создайте файл /lib/systemd/system/_имя_сервиса_.service
2. В тексте файла укажите:
    ```
    [Unit]
    Description=**название**
    After=multi-user.target
    
    [Service]
    Type=idle
    ExecStart=**путь_к_интерпретатору_env** **путь_к_файлу_скрипта**
    
    [Install]
    WantedBy=multi-user.target
    ```
3. Дайте разрешение файлу-сервиса
    ```sudo chmod 644 /lib/systemd/system/**имя_сервиса**.service```
4. Запустите сервис:
   ```
   sudo systemctl daemon-reload
   sudo systemctl enable **имя_сервиса**.service
   sudo reboot
   ```
5. Для работы с сервисом:
   ```
   sudo systemctl enable **имя_сервиса**.service  - разрешить выполнение
   sudo systemctl start **имя_сервиса**.service  - запустить
   sudo systemctl status **имя_сервиса**.service  - статус
   sudo systemctl stop **имя_сервиса**.service  - остановить
   sudo systemctl disable **имя_сервиса**.service  - запретить выполнение
   ```
