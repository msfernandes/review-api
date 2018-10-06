from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from datetime import datetime
from core import models


User = get_user_model()


class TestReviewViewSet(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name='John', last_name='Doe',
                                        email='john@doe.com', username='john')
        self.user2 = User.objects.create(first_name='Doe', last_name='John',
                                         email='doe@john.com', username='doe')
        self.company = models.Company.objects.create(name='Company')
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_should_return_only_authored_reviews(self):
        timestamp = datetime.now()
        models.Review.objects.create(
            rating=1, title='title', summary='summary',
            ip='127.0.0.1', company=self.company, reviewer=self.user,
            submission_date=timestamp
        )
        models.Review.objects.create(
            rating=1, title='title', summary='summary',
            ip='127.0.0.1', company=self.company, reviewer=self.user2,
            submission_date=timestamp
        )

        response = self.client.get(reverse('review-list'), format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.json()), 1)

    def test_should_return_not_allowed(self):
        response = self.client.put(reverse('review-list'), format='json')
        self.assertEquals(response.status_code,
                          status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.delete(reverse('review-list'), format='json')
        self.assertEquals(response.status_code,
                          status.HTTP_405_METHOD_NOT_ALLOWED)
