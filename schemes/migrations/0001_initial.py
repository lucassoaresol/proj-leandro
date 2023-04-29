# Generated by Django 4.2 on 2023-04-29 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
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
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schemes",
                        to="departments.department",
                    ),
                ),
            ],
        ),
    ]