# Generated by Django 3.0.1 on 2020-03-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='blogs/%Y/%m/%d'),
        ),
    ]
