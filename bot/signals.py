from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone

from bot.bot import bot
from bot.models import TelegramSubscriber


@receiver(user_logged_in)
def notify_admin_login(sender, request, user, **kwargs):
    if request.path.startswith('/admin/'):
        date_str = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f'✅ Вход в админку\nДата: {date_str}\nПользователь: {user.username}'
        for subscriber in TelegramSubscriber.objects.all():
            try:
                bot.send_message(subscriber.user_id, message)
            except Exception as e:
                pass
