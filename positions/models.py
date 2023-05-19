from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=150)

    departments = models.ManyToManyField(
        "departments.Department",
        related_name="positions",
    )
