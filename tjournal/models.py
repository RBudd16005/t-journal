from django.db import models
import datetime


class Report(models.Model):
    date = models.DateField(default=datetime.date.today)
    breakfast = models.BooleanField(default=False)
    healthy = models.BooleanField(default=False)
    shower = models.BooleanField(default=False)
    exercise = models.BooleanField(default=False)
    sleep = models.IntegerField(default=0)
    clothes = models.CharField(max_length=15, default="Casual")
    start = models.TimeField(default=datetime.datetime.now)
    rules = models.BooleanField(default=False)
    money = models.DecimalField(decimal_places=2, max_digits=1000)
