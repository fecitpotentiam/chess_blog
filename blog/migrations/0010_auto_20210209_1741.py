# Generated by Django 3.1.6 on 2021-02-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_event_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='Изображение'),
        ),
    ]
