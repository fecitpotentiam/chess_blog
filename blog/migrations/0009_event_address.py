# Generated by Django 3.1.6 on 2021-02-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210209_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(blank=True, max_length=300, verbose_name='Место проведения'),
        ),
    ]
