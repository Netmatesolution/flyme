# Generated by Django 4.0 on 2021-12-23 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='tourimg')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour')),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('highlights', models.TextField(blank=True, null=True)),
                ('visited_places', models.CharField(max_length=1000)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour')),
            ],
        ),
    ]
