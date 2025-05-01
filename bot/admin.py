from django.contrib import admin

from .models import TelegramSubscriber


@admin.register(TelegramSubscriber)
class TelegramSubscriberAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'subscribed_at')
    ordering = ('-subscribed_at',)
    search_fields = ('user_id',)
