from django.db import models


class TelegramSubscriber(models.Model):
    user_id = models.BigIntegerField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)
