from django.db import models


class Criterion(models.Model):
    description = models.TextField()
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="criterions",
    )
