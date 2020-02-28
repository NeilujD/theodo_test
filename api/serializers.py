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

        start_date = data.get('start_date')
        end_date = data.get('end_date')
        runner = data.get('runner')

        if start_date > end_date:
            raise serializers.ValidationError("`end_date` must occur after `start_date`")

        runs = Run.objects.filter(end_date__gte=start_date, runner=runner)
        if len(runs) > 0:
            raise serializers.ValidationError("new user run have to start after the last one")

        return data