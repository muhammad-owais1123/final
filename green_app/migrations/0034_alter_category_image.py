# Generated by Django 5.0.7 on 2024-08-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0033_orderdetails_grandtotal"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(max_length=255, upload_to="categories/"),
        ),
    ]
