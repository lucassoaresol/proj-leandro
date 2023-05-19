from django.db import models


class Option(models.Model):
    name = models.CharField(max_length=150)
    value = models.IntegerField()

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="options",
    )
