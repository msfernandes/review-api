from rest_framework.authtoken.models import Token


def create_user_token(sender, instance, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
