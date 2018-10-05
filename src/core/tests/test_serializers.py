from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from core import models, serializers
from unittest.mock import Mock


User = get_user_model()


class TestReviewSerializer(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name='John', last_name='Doe',
                                        email='john@doe.com', username='john')
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_should_create_review(self):
        data = {
            'rating': 1,
            'title': 'title',
            'summary': 'summary',
            'company': {
                'name': 'Company'
            }
        }
        response = self.client.post(
            reverse('review-list'),
            data,
            format='json'
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(models.Review.objects.count(), 1)
        self.assertEquals(models.Review.objects.get().rating, 1)

    def test_should_show_rating_error(self):
        data = {
            'rating': 10,
            'title': 'title',
            'summary': 'summary',
            'company': {
                'name': 'Company'
            }
        }
        response = self.client.post(
            reverse('review-list'),
            data,
            format='json'
        )
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(models.Review.objects.count(), 0)

    def test_create_method(self):
        data = {
            'rating': 1,
            'title': 'title',
            'summary': 'summary',
            'company': {
                'name': 'Company'
            }
        }

        mock_methods = {
            'META.get.return_value': '127.0.0.1',
            'user': self.user
        }
        mock = Mock()
        mock.configure_mock(**mock_methods)

        serializer = serializers.ReviewSerializer()
        serializer.context['request'] = mock
        review = serializer.create(data)
        self.assertEquals(review.ip, '127.0.0.1')
        self.assertEquals(review.reviewer, self.user)
        self.assertEquals(models.Review.objects.count(), 1)
