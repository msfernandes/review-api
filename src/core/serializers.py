from rest_framework import serializers
from core import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('id', 'name')


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserSerializer(read_only=True)
    company = CompanySerializer()

    class Meta:
        model = models.Review
        fields = ('id', 'rating', 'title', 'summary', 'ip', 'company',
                  'reviewer', 'submission_date')
