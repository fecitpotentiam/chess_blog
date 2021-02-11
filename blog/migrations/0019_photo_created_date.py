# Generated by Django 3.1.6 on 2021-02-09 18:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_photoalbum_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]