from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


User = get_user_model()


class TestReview(TestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='John', last_name='Doe',
                                        email='john@doe.com', username='john')
        self.company = models.Company.objects.create(name='Company')

    def test_str(self):
        review = models.Review.objects.create(
            rating=1,
            title='Title',
            summary='Summary',
            ip='127.0.0.1',
            company=self.company,
            reviewer=self.user,
        )
        self.assertEquals(review.__str__(), 'Title')


class TestCompany(TestCase):

    def test_str(self):
        company = models.Company.objects.create(name='Company')
        self.assertEquals(company.__str__(), 'Company')
