# Generated by Django 4.0 on 2022-03-05 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0010_activity_what_to_expect'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='video_link',
            new_name='video_id',
        ),
    ]
