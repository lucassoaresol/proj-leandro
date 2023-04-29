from django.db import models


class Request(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    canceled_at = models.DateField(null=True)

    scheme = models.ForeignKey(
        "schemes.Scheme",
        on_delete=models.CASCADE,
        related_name="requests",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="requests",
    )

    criterion = models.ForeignKey(
        "criterions.Criterion",
        on_delete=models.CASCADE,
        related_name="requests",
    )
