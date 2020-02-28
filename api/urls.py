from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as tokenviews

from . import views


router = routers.DefaultRouter()
router.register(r'runs', views.RunViewSet)

urlpatterns = [
    path('token-auth/', tokenviews.obtain_auth_token),
    path('statistics/', views.StatisticsView.as_view()),
    path('', include(router.urls))
]