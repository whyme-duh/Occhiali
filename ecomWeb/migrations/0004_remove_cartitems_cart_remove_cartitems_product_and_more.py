# Generated by Django 4.2.1 on 2023-06-04 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomWeb', '0003_remove_cart_active_cart_is_paid_cartitems'),
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
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItems',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
