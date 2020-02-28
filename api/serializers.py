from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Run

User = get_user_model()


class RunSerializer(serializers.HyperlinkedModelSerializer):
    runner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Run
        fields = ['start_date', 'end_date', 'distance', 'burnt_calories', 'runner']