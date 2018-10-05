from django.test import TestCase
from django.contrib.auth import get_user_model
from contextlib import contextmanager
from rest_framework.authtoken.models import Token


User = get_user_model()


class TestCreateTokenSignal(TestCase):

    @contextmanager
    def assertNotRaises(self, exc_type):
        try:
            yield None
        except exc_type:
            raise self.failureException('{} raised'.format(exc_type.__name__))

    def test_should_create(self):
        user = User.objects.create(first_name='John', last_name='Doe',
                                   email='john@doe.com')
        with self.assertNotRaises(Token.DoesNotExist):
            token = Token.objects.get(user=user)
            self.assertEquals(token.user, user)
