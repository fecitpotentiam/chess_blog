# Generated by Django 3.1.6 on 2021-02-23 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20210223_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('link', models.CharField(max_length=256, verbose_name='Ссылка')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Ссылка на материал',
                'verbose_name_plural': 'Ссылки на материалы',
            },
        ),
    ]