from rest_framework import serializers

from .models import Run


class RunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Run
        fields = ['start_date', 'end_date', 'distance', 'burn_calories', 'runner']