# Generated by Django 5.0.7 on 2024-08-31 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0050_orderdetails_paymentstatus"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderdetails",
            name="paymentStatus",
            field=models.CharField(
                choices=[("paid", "Paid"), ("Pending", "pending"), ("COD", "cod")],
                max_length=7,
                null=True,
            ),
        ),
    ]
