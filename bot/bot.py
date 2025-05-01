import telebot
from django.conf import settings

from bot.models import TelegramSubscriber

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def handle_subscribe(message):
    user_id = message.chat.id
    TelegramSubscriber.objects.get_or_create(user_id=user_id)
    bot.send_message(
        user_id, 'Вы подписались на уведомления о входе в админку.'
    )
