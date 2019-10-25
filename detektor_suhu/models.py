
# Create your models here.
from django.db import models


class Stats(models.Model):
    suhu = models.fields.FloatField()
    humidity = models.fields.FloatField()
