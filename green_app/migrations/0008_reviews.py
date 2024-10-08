# Generated by Django 5.0.7 on 2024-08-15 14:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0007_orderdetails"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reviews",
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
                (
                    "ratings",
                    models.PositiveIntegerField(
                        help_text="Rate between 1 (lowest) to 5 (highest)",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                ("description", models.CharField(max_length=300)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="reviews/images/"
                    ),
                ),
                (
                    "products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="green_app.product",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="green_app.profile",
                    ),
                ),
            ],
        ),
    ]
