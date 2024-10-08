# Generated by Django 5.0.7 on 2024-08-10 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0002_wishlist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="wishlist",
            name="product",
        ),
        migrations.CreateModel(
            name="Items",
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
                ("color", models.CharField(max_length=30)),
                ("drainage", models.CharField(max_length=3)),
                ("gloss", models.CharField(max_length=4)),
                ("quantity", models.IntegerField(blank=True, null=True)),
                (
                    "prodInfo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="green_app.productinfo",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="wishlist",
            name="items",
            field=models.ManyToManyField(to="green_app.items"),
        ),
    ]
