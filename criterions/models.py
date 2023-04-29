from django.db import models


class Criterion(models.Model):
    value = models.IntegerField()
    description = models.TextField()
