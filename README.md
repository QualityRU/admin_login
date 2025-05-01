# Django Telegram Bot Notifier

## Описание
Этот проект отправляет сообщение всем пользователям, подписавшимся на Telegram-бота, о каждом успешном входе пользователя в админку Django. Сообщение содержит дату входа и имя пользователя.

## Используемые технологии
- Django==5.2
- pyTelegramBotAPI==4.26.0
- python-decouple==3.8

## Установка и настройка
1. Клонируйте репозиторий
```
git clone https://github.com/QualityRU/admin_login.git
cd admin_login
```
2. Создайте виртуальное окружение
```
python -m venv venv
```
3. Активируйте виртуальное окружение
```
. venv/bin/activate
```
4. Установите зависимости
```
pip install -r requirements.txt
```
5. Создайте файл .env
```
DEBUG=True
SECRET_KEY=your_django_secret_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
```
6. Примените миграции
```
python manage.py makemigrations
python manage.py migrate
```
7. Создайте суперпользователя
```
python manage.py createsuperuser
```
8. Запустите сервер
```
python manage.py runserver
```
9. Запустите бота
```
python runbot.py
```
10. Проверьте, что всё работает

- Перейдите в админку Django на http://127.0.0.1:8000/admin/
- Войдите как суперпользователь.
- Убедитесь, что подписчики бота получают сообщение о вашем входе.
