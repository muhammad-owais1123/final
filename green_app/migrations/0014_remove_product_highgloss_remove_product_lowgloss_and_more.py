# Generated by Django 5.0.7 on 2024-08-18 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0013_product_inventory"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="highgloss",
        ),
        migrations.RemoveField(
            model_name="product",
            name="lowgloss",
        ),
        migrations.AddField(
            model_name="productinfo",
            name="gloss",
            field=models.CharField(
                choices=[("High", "high"), ("Low", "low")], max_length=20, null=True
            ),
        ),
    ]
