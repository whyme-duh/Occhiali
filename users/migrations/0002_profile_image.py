# Generated by Django 4.2.1 on 2023-05-28 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile/default.jpg', upload_to='profile'),
        ),
    ]
