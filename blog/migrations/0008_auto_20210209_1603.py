# Generated by Django 3.1.6 on 2021-02-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='event',
            name='payment',
            field=models.CharField(blank=True, max_length=100, verbose_name='Взнос'),
        ),
    ]