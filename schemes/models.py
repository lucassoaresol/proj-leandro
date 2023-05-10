from django.db import models


class Status(models.TextChoices):
    OPEN = "Open"
    FINISHED = "Finished"
    CANCELED = "Canceled"


class Scheme(models.Model):
    name = models.CharField(max_length=150)
    min_criterion = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN,
    )
    created_at = models.DateField(auto_now_add=True)
    finished_at = models.DateField(null=True)

    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name="schemes",
    )
