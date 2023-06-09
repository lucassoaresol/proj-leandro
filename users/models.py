from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    ADMINISTRATOR = "Administrator"
    MANAGER = "Manager"
    COMMON = "Common"


class User(AbstractUser):
    phone = models.CharField(max_length=150, default="")
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.COMMON,
    )
    is_active = models.BooleanField(default=False)
    is_first_access = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)
    date_expired = models.DateTimeField(null=True)

    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name="users",
    )

    position = models.ForeignKey(
        "positions.Position",
        on_delete=models.CASCADE,
        related_name="users",
    )
