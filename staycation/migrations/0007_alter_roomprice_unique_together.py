# Generated by Django 4.0 on 2021-12-25 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('staycation', '0006_alter_staycationroom_room_name_roomprice'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='roomprice',
            unique_together={('staycation', 'room_name', 'number_of_nights', 'host_id')},
        ),
    ]
