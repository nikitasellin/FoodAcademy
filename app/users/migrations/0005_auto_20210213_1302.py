# Generated by Django 3.1.5 on 2021-02-13 10:02

from django.db import migrations
import easy_thumbnails.fields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210206_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='/static/images/teacher/avatar.png', upload_to=users.models.unique_file_name, verbose_name='Аватар'),
        ),
    ]
