# Generated by Django 5.0.7 on 2024-08-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0024_alter_profile_cart_alter_profile_wishlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productinfo",
            name="image",
            field=models.ImageField(
                blank=True, max_length=255, null=True, upload_to="products/"
            ),
        ),
    ]
