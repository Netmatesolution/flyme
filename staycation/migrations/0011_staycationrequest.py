# Generated by Django 4.0 on 2021-12-29 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('staycation', '0010_alter_roomprice_room_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaycationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('user_email', models.CharField(blank=True, max_length=100, null=True)),
                ('user_number', models.CharField(blank=True, max_length=100, null=True)),
                ('checkin', models.DateField(blank=True, null=True)),
                ('checkout', models.DateField(blank=True, null=True)),
                ('numberofnights', models.IntegerField(blank=True, null=True)),
                ('adult', models.IntegerField(blank=True, null=True)),
                ('child', models.IntegerField(blank=True, null=True)),
                ('occassion', models.CharField(blank=True, max_length=100, null=True)),
                ('host_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staycation.staycationroom')),
                ('staycation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staycation.staycation')),
            ],
        ),
    ]