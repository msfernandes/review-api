from rest_framework import routers
from django.urls import path, include
from core import views


router = routers.DefaultRouter()
router.register('reviews', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
