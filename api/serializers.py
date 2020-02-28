from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Run

User = get_user_model()


class RunSerializer(serializers.HyperlinkedModelSerializer):
    runner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Run
        fields = ['start_date', 'end_date', 'distance', 'burnt_calories', 'runner']

    def validate(self, data):
        """
            Check that start_date is before end_date.
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("`end_date` must occur after `start_date`")
        return data