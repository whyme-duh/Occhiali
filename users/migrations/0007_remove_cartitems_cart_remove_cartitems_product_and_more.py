# Generated by Django 4.2.1 on 2023-06-10 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_phone_alter_cartitems_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItems',
        ),
    ]
