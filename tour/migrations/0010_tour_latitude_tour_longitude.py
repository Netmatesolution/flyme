# Generated by Django 4.0 on 2022-04-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0009_days_slug_alter_days_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='latitude',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='longitude',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
