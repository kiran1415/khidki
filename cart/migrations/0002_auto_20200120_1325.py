# Generated by Django 2.2.7 on 2020-01-20 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='date_added',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]