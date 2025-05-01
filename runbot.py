import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_login.settings')
django.setup()

from bot.bot import bot

bot.polling(none_stop=True)
