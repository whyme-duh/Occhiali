# Generated by Django 4.2.1 on 2023-06-13 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomWeb', '0013_delete_buynow'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_completed',
            field=models.BooleanField(default=False),
        ),
    ]
