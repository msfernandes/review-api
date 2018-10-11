from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from core import views


router = routers.DefaultRouter()
router.register('reviews', views.ReviewViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/token/', obtain_auth_token)
]
