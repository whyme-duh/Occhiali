# Generated by Django 4.2.1 on 2023-09-04 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomWeb', '0014_order_payment_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='message',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_id',
        ),
    ]
