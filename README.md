# Agregator_bot

Телеграм-бот, выдающий по запросу пользователя топ учебных курсов по IT-направлениям с указанием цены

## Структура (на текущий момент)

- bot.py - Основное тело бота
- main_dialog.py - реализация основной линии диалога с пользователем 
- База данных Postgresql
- utils.py - вспомогательные функции, генерации клавиатур и списков курсов из базы, ранжирование 
- texts - Все тексты на кнопках

## Что уже реализовано 
- Основная линия диалога с пользователем
- Вывод учебных направлений 
- Вывод отсортированных по запросу пользователя курсов (пока не топ-10, так как база мало заполнена)
- Линия диалога для помощи в определении учебного направления
- Возможность возврата к предыдущему вопросу 

## Что планируется 
- Вывести бота на сервер
- Добавить запись конкретного пользователя
- Парсить данные с агрегаторов 
- Покрыть тестированием 
- Высылать автоматизированные напоминалки тем, кто не смог определиться при появлении новых курсов или направлений

## Эволюция проекта 
- Сначала все функции выполнялись отдельными хендлерами-> перешли на CallbackQuery 
- Данные собирались из написанныйх вручную массивов -> реализовали заполнение данных в БД (далее планируется парсинг)
- Клавиатуры генерились прямо в функциях -> вынести все в отдельных файл utils 

## Библиотеки 
- logging - логирование
- SQLAlchemy - для работы с БД 
- telegram - для работы с Телеграм
- csv - работа с csv файлами

## Установка

1. Копируйте репозиторий с гитхаб
2. Cоздайте виртуальное окружение
3. установите зависимости командой `pip install -r requirements.txt`

4. Создайте файл `settings.py`

5. Впишите туда (прокси необязателен)
```
API_KEY = "ваш ключ бота"
PROXY_URL = "socks5://t1.learn.python.ru:1080"
PROXY_USERNAME = "learn"
PROXY_PASSWORD = "python"
```
6. Запустите бота командой `python bot.py`
