from rest_framework import serializers
from core import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('id', 'name')


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserSerializer(read_only=True)
    company = CompanySerializer()
    ip = serializers.IPAddressField(protocol='both', read_only=True)
    submission_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.Review
        fields = ('id', 'rating', 'title', 'summary', 'ip', 'company',
                  'reviewer', 'submission_date')

    def create(self, validated_data):
        request = self.context['request']
        client_ip = request.META.get('REMOTE_ADDR')
        validated_data['ip'] = client_ip

        validated_data['reviewer'] = request.user

        company_data = validated_data.pop('company')
        company = models.Company.objects.get_or_create(
            name=company_data.get('name')
        )[0]
        validated_data['company'] = company

        return super().create(validated_data)
