# Generated by Django 4.0 on 2021-12-24 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_days_tournew'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='days',
            name='tournew',
        ),
    ]
