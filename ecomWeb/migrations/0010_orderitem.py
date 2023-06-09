# Generated by Django 4.2.1 on 2023-06-10 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomWeb', '0009_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomWeb.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomWeb.product')),
            ],
        ),
    ]
