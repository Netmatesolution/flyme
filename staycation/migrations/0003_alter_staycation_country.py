# Generated by Django 4.0 on 2021-12-24 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('staycation', '0002_remove_staycation_image1_remove_staycation_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staycation',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.country'),
        ),
    ]
