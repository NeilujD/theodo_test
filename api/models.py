from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Run(models.Model):
    """
        Run django model class
    """
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    distance = models.FloatField()
    burnt_calories = models.IntegerField()

    runner = models.ForeignKey(User, on_delete=models.CASCADE)