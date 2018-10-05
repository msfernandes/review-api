from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_save


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from core import signals
        post_save.connect(signals.create_user_token,
                          sender=settings.AUTH_USER_MODEL)
