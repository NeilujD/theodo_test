from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as tokenviews

from . import views


router = routers.DefaultRouter()
router.register(r'runs', views.RunViewSet)

urlpatterns = [
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token-auth/', tokenviews.obtain_auth_token),
    path('', include(router.urls))
]