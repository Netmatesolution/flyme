# Generated by Django 4.0 on 2021-12-31 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_customtrip_departure_remove_customtrip_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='country'),
        ),
    ]
