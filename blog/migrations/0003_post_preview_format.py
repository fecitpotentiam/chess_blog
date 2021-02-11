# Generated by Django 3.1.6 on 2021-02-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_preview_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_format',
            field=models.CharField(choices=[('S', 'Стандартный'), ('G', 'Галерея'), ('W', 'Без изображения')], default='S', max_length=1),
        ),
    ]