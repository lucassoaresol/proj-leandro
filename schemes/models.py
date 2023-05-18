from django.db import models


class Status(models.TextChoices):
    OPEN = "Open"
    FINISHED = "Finished"
    CANCELED = "Canceled"


class Scheme(models.Model):
    name = models.CharField(max_length=150)
    num_criterion = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN,
    )
    created_at = models.DateField(auto_now_add=True)
    finished_at = models.DateField(null=True)

    departments = models.ManyToManyField(
        "departments.Department",
        related_name="schemes",
    )

    positions = models.ManyToManyField(
        "positions.Position",
        related_name="schemes",
    )
