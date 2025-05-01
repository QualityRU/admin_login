from django.test import TestCase

from bot.models import TelegramSubscriber


class SubscriptionTestCase(TestCase):
    def test_create_subscriber(self):
        TelegramSubscriber.objects.create(user_id=123456)
        self.assertTrue(
            TelegramSubscriber.objects.filter(user_id=123456).exists()
        )
