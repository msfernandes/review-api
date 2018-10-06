from rest_framework import viewsets
from core.models import Review
from core.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        return Review.objects.filter(reviewer=self.request.user)
