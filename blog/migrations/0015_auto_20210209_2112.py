# Generated by Django 3.1.6 on 2021-02-09 16:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_event_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
    ]
