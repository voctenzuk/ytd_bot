# Generated by Django 2.2.10 on 2020-03-03 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0013_auto_20200222_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='last_video_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Публикация последнего видео'),
        ),
        migrations.AlterField(
            model_name='video',
            name='upload_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
    ]
