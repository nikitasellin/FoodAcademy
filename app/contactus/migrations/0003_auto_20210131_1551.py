# Generated by Django 3.1.5 on 2021-01-31 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0002_auto_20210131_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='received_at',
            new_name='received_time',
        ),
    ]
