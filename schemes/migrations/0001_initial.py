# Generated by Django 4.2 on 2023-05-18 05:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("positions", "0001_initial"),
        ("departments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Scheme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("num_criterion", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Open", "Open"),
                            ("Finished", "Finished"),
                            ("Canceled", "Canceled"),
                        ],
                        default="Open",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("finished_at", models.DateField(null=True)),
                (
                    "departments",
                    models.ManyToManyField(
                        related_name="schemes", to="departments.department"
                    ),
                ),
                (
                    "positions",
                    models.ManyToManyField(
                        related_name="schemes", to="positions.position"
                    ),
                ),
            ],
        ),
    ]
