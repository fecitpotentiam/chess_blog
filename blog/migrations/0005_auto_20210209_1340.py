# Generated by Django 3.1.6 on 2021-02-09 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210209_1338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Запись в блоге', 'verbose_name_plural': 'Записи в блоге'},
        ),
    ]
