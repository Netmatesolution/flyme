# Generated by Django 4.0 on 2021-12-31 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staycation', '0012_alter_staycation_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staycationrequest',
            name='checkin',
        ),
        migrations.RemoveField(
            model_name='staycationrequest',
            name='checkout',
        ),
        migrations.AddField(
            model_name='staycationrequest',
            name='tour_dates',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]