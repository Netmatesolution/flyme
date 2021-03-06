# Generated by Django 4.0 on 2021-12-26 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('package_name', models.CharField(max_length=100)),
                ('activity_duration', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('inclusions', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('mon', models.BooleanField(default=False)),
                ('tue', models.BooleanField(default=False)),
                ('wed', models.BooleanField(default=False)),
                ('thu', models.BooleanField(default=False)),
                ('fri', models.BooleanField(default=False)),
                ('sat', models.BooleanField(default=False)),
                ('sun', models.BooleanField(default=False)),
                ('activity_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.activity')),
                ('host_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
